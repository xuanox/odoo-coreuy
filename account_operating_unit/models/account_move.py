# -*- coding: utf-8 -*-
# © 2016 Eficent Business and IT Consulting Services S.L.
# © 2016 Serpent Consulting Services Pvt. Ltd.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from openerp.tools.translate import _
from openerp import api, fields, models
from openerp.exceptions import ValidationError


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    operating_unit_id = fields.Many2one('operating.unit', 'Operating Unit',
                                        default=lambda self:
                                        self.env['res.users'].
                                        operating_unit_default_get(self._uid))

    @api.model
    def create(self, vals):
        if not vals.get('operating_unit_id', False):
            voucher_line = self._context.get('voucher_line', False)
            voucher = self._context.get('voucher', False)
            if voucher_line:
                vals['operating_unit_id'] = voucher_line.operating_unit_id.id
            elif voucher:
                vals['operating_unit_id'] = voucher.operating_unit_id.id
            elif vals.get('move_id', False):
                move = self.env['account.move'].browse(vals['move_id'])
                if move.operating_unit_id:
                    vals['operating_unit_id'] = move.operating_unit_id.id
        _super = super(AccountMoveLine, self)
        return _super.create(vals)

    #MVARELA sustituido para v8
    # @api.model
    # def _query_get(self, domain=None):
    #     if domain is None:
    #         domain = []
    #     if self._context.get('operating_unit_ids', False):
    #         domain.append(('operating_unit_id', 'in',
    #                        self._context.get('operating_unit_ids')))
    #     return super(AccountMoveLine, self)._query_get(domain)

    #MVARELA sustituido para v8
    @api.model
    def _query_get(self, obj='l'):
        res = super(AccountMoveLine, self)._query_get(obj=obj)
        if self._context.get('operating_unit_ids', False):
            if res:
                res += " AND "
            if len(self._context.get('operating_unit_ids', False)) > 1:
                res += obj+".operating_unit_id in %s" % (tuple(self._context.get('operating_unit_ids')),)
            else:
                res += obj+".operating_unit_id = %s" % (self._context.get('operating_unit_ids')[0])
        return res

    @api.multi
    @api.constrains('operating_unit_id', 'company_id')
    def _check_company_operating_unit(self):
        self = self.sudo()
        for rec in self:
            if (rec.company_id and rec.operating_unit_id and rec.company_id !=
                    rec.operating_unit_id.company_id):
                raise ValidationError(_('Configuration error!\nThe Company in the'
                                  ' Move Line and in the Operating Unit must '
                                  'be the same.'))

    #Se comenta control ya que se pueden crear asientos con lineas de diferentes operating unit
    # @api.multi
    # @api.constrains('operating_unit_id', 'move_id')
    # def _check_move_operating_unit(self):
    #     for rec in self:
    #         if (rec.move_id and rec.move_id.operating_unit_id and
    #             rec.operating_unit_id and rec.move_id.operating_unit_id !=
    #                 rec.operating_unit_id):
    #             raise ValidationError(_('Configuration error!\nThe Operating Unit in'
    #                               ' the Move Line and in the Move must be the'
    #                               ' same.'))


class AccountMove(models.Model):
    _inherit = "account.move"

    operating_unit_id = fields.Many2one('operating.unit',
                                        'Default operating unit', states={'posted':[('readonly',True)]},
                                        help="This operating unit will "
                                             "be defaulted in the move lines.")

    # RAGU asegurarse de buscar UE en caso de no venir por parametros
    @api.model
    def create(self, vals):
        if not vals.get('operating_unit_id', False):
            voucher_line = self._context.get('voucher_line', False)
            voucher = self._context.get('voucher', False)
            if voucher:
                vals['operating_unit_id'] = voucher.operating_unit_id.id
            elif voucher_line:
                vals['operating_unit_id'] = voucher_line.operating_unit_id.id
        return super(AccountMove, self).create(vals)

    @api.multi
    def _prepare_inter_ou_balancing_move_line(self, move, ou_id,
                                              ou_balances):
        if not move.company_id.inter_ou_clearing_account_id:
            raise ValidationError(_('Error!\nYou need to define an inter-operating\
                unit clearing account in the company settings'))

        res = {
            'name': 'Balanceo-UE',
            'move_id': move.id,
            'journal_id': move.journal_id.id,
            'date': move.date,
            'operating_unit_id': ou_id,
            'account_id': move.company_id.inter_ou_clearing_account_id.id,
            # irabaza => Enviar 'period_id' por vals en la creación de move_lines para evitar error!!
            'period_id': move.period_id.id
        }

        if ou_balances[ou_id] < 0.0:
            res['debit'] = abs(ou_balances[ou_id])

        else:
            res['credit'] = ou_balances[ou_id]
        return res

    @api.multi
    def _check_ou_balance(self, move):
        # Look for the balance of each OU
        ou_balance = {}
        for line in move.line_id:
            if line.operating_unit_id.id not in ou_balance:
                ou_balance[line.operating_unit_id.id] = 0.0
            ou_balance[line.operating_unit_id.id] += (line.debit - line.credit)
        return ou_balance

    @api.multi
    def post(self):
        ml_obj = self.env['account.move.line']
        for move in self:
            if not move.company_id.ou_is_self_balanced:
                continue

            # If all move lines point to the same operating unit, there's no
            # need to create a balancing move line
            ou_list_ids = [line.operating_unit_id and
                           line.operating_unit_id.id for line in
                           move.line_id if line.operating_unit_id]
            if len(ou_list_ids) <= 1:
                continue

            # Create balancing entries for un-balanced OU's.
            ou_balances = self._check_ou_balance(move)
            amls = []
            for ou_id in ou_balances.keys():
                # If the OU is already balanced, then do not continue
                if move.company_id.currency_id.is_zero(ou_balances[ou_id]):
                    continue
                # Create a balancing move line in the operating unit
                # clearing account
                line_data = self._prepare_inter_ou_balancing_move_line(
                    move, ou_id, ou_balances)
                if line_data:
                    amls.append(ml_obj.with_context(wip=True).
                                create(line_data))
            if amls:
                move.with_context(wip=False).\
                    write({'line_id': [(4, aml.id) for aml in amls]})

        return super(AccountMove, self).post()

    def assert_balanced(self):
        if self.env.context.get('wip'):
            return True
        return super(AccountMove, self).assert_balanced()

    @api.multi
    @api.constrains('line_id')
    def _check_ou(self):
        for move in self:
            if not move.company_id.ou_is_self_balanced:
                continue
            for line in move.line_id:
                if not line.operating_unit_id:
                    raise ValidationError(_('Configuration error!\nThe operating\
                    unit must be completed for each line if the operating\
                    unit has been defined as self-balanced at company level.'))
