# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Enterprise Management Solution
#    GRP Estado Uruguay
#    Copyright (C) 2017 Quanam (ATEL SA., Uruguay)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from base import SoapClientBase

class SoapSiceOrdenCompra(SoapClientBase):
    """ GRP SICE Web Service Orden Compra """

    #Begin Alta -------------------------------------------------------------------------------------------------
    def _prepare_request_alta(self, post_data):
        """
            @params post_data:
                {
                    See Documentation: Canal de Compras - Integración GRPs -v3.pdf. Page: 151
                }
        """
        return post_data

    def request_alta(self, model, cr, uid, ids, post_data, context=None):
        """
            Método que ejecuta el servicio de orden compra: alta
            @see _prepare_request_alta
        """
        if not isinstance(post_data, (dict,)):
            raise Exception("Se espera un diccionario como valor de retorno. Se ha recibido el tipo: %s" % (type(post_data),))
        url = model.pool.get('ir.config_parameter').get_param(cr, uid, 'url_ws.sice_orden_compras', context=context)
        if not url:
            raise Exception(u'No se encuentra configurada la conexión con SICE.\n \
                Ir a: Configuración -> Parámetros -> Parámetros del sistema y cargar un registro \
                con clave url_ws.sice_orden_compras y valor la URL del servicio web.')
        self.ensure_connection(url=url, msg_attr = 'Servicio: Orden Compra > Alta')
        _request = self._prepare_request_alta(post_data)
        #Response
        return self.client.service.alta(_request)
    #End Alta ---------------------------------------------------------------------------------------------------

    #Begin Alta con Atributos -----------------------------------------------------------------------------------
    def _prepare_request_alta_attr(self, post_data):
        """
            @params post_data:
                {
                    See Documentation: Canal de Compras - Integración GRPs -v3.pdf. Page: 156
                }
        """
        return post_data

    def request_alta_attr(self, model, cr, uid, ids, post_data, context=None):
        """
            Método que ejecuta el servicio de orden compra: alta con atributos
            @see _prepare_request_alta_attr
        """
        if not isinstance(post_data, (dict,)):
            raise Exception("Se espera un diccionario como valor de retorno. Se ha recibido el tipo: %s" % (type(post_data),))
        url = model.pool.get('ir.config_parameter').get_param(cr, uid, 'url_ws.sice_orden_compras', context=context)
        if not url:
            raise Exception(u'No se encuentra configurada la conexión con SICE.\n \
                Ir a: Configuración -> Parámetros -> Parámetros del sistema y cargar un registro \
                con clave url_ws.sice_orden_compras y valor la URL del servicio web.')
        self.ensure_connection(url=url, msg_attr = 'Servicio: Orden Compra > Alta con Atributos')
        _request = self._prepare_request_alta_attr(post_data)
        #Response
        return self.client.service.altaConAtributos(_request)
    #End Alta con Atributos ---------------------------------------------------------------------------------------

    #Begin Modificar ----------------------------------------------------------------------------------------------
    def _prepare_request_modificar(self, post_data):
        """
            @params post_data:
                {
                    See Documentation: Canal de Compras - Integración GRPs -v3.pdf. Page: 157
                }
        """
        return post_data

    def request_modificar(self, model, cr, uid, ids, post_data, context=None):
        """
            Método que ejecuta el servicio de orden compra: modificar
            @see _prepare_request_modificar
        """
        if not isinstance(post_data, (dict,)):
            raise Exception("Se espera un diccionario como valor de retorno. Se ha recibido el tipo: %s" % (type(post_data),))
        url = model.pool.get('ir.config_parameter').get_param(cr, uid, 'url_ws.sice_orden_compras', context=context)
        if not url:
            raise Exception(u'No se encuentra configurada la conexión con SICE.\n \
                Ir a: Configuración -> Parámetros -> Parámetros del sistema y cargar un registro \
                con clave url_ws.sice_orden_compras y valor la URL del servicio web.')
        self.ensure_connection(url=url, msg_attr = 'Servicio: Orden Compra > Modificar')
        _request = self._prepare_request_modificar(post_data)
        #Response
        return self.client.service.modificar(_request)
    #End Modificar --------------------------------------------------------------------------------------------------

    #Begin Modificar con Atributos ----------------------------------------------------------------------------------
    def _prepare_request_modificar_attr(self, post_data):
        """
            @params post_data:
                {
                    See Documentation: Canal de Compras - Integración GRPs -v3.pdf. Page: 160
                }
        """
        return post_data

    def request_modificar_attr(self, model, cr, uid, ids, post_data, context=None):
        """
            Método que ejecuta el servicio de orden compra: modificar con atributos
            @see _prepare_request_modificar_attr
        """
        if not isinstance(post_data, (dict,)):
            raise Exception("Se espera un diccionario como valor de retorno. Se ha recibido el tipo: %s" % (type(post_data),))
        url = model.pool.get('ir.config_parameter').get_param(cr, uid, 'url_ws.sice_orden_compras', context=context)
        if not url:
            raise Exception(u'No se encuentra configurada la conexión con SICE.\n \
                Ir a: Configuración -> Parámetros -> Parámetros del sistema y cargar un registro \
                con clave url_ws.sice_orden_compras y valor la URL del servicio web.')
        self.ensure_connection(url=url, msg_attr = 'Servicio: Orden Compra > Modificar con Atributos')
        _request = self._prepare_request_modificar_attr(post_data)
        #Response
        return self.client.service.modificarConAtributos(_request)
    #End Modificar con atributos -------------------------------------------------------------------------------------

    #Begin Eliminar -----------------------------------------------------------------------------------------------
    def _prepare_request_eliminar(self, post_data):
        """
            @params post_data:
                {
                    See Documentation: Canal de Compras - Integración GRPs -v3.pdf. Page: 160
                }
        """
        return post_data

    def request_eliminar(self, model, cr, uid, ids, post_data, context=None):
        """
            Método que ejecuta el servicio de orden compra: eliminar
            @see _prepare_request_eliminar
        """
        if not isinstance(post_data, (dict,)):
            raise Exception("Se espera un diccionario como valor de retorno. Se ha recibido el tipo: %s" % (type(post_data),))
        url = model.pool.get('ir.config_parameter').get_param(cr, uid, 'url_ws.sice_orden_compras', context=context)
        if not url:
            raise Exception(u'No se encuentra configurada la conexión con SICE.\n \
                Ir a: Configuración -> Parámetros -> Parámetros del sistema y cargar un registro \
                con clave url_ws.sice_orden_compras y valor la URL del servicio web.')
        self.ensure_connection(url=url, msg_attr = 'Servicio: Orden Compra > Eliminar')
        _request = self._prepare_request_eliminar(post_data)
        #Response
        return self.client.service.eliminar(_request)
    #End Eliminar -------------------------------------------------------------------------------------------------

    #Begin Aprobar -----------------------------------------------------------------------------------------------
    def _prepare_request_aprobar(self, post_data):
        """
            @params post_data:
                {
                    See Documentation: Canal de Compras - Integración GRPs -v3.pdf. Page: 161
                }
        """
        return post_data

    def request_aprobar(self, model, cr, uid, ids, post_data, context=None):
        """
            Método que ejecuta el servicio de orden compra: aprobar
            @see _prepare_request_aprobar
        """
        # if not isinstance(post_data, (dict,)):
        #     raise Exception("Se espera un diccionario como valor de retorno. Se ha recibido el tipo: %s" % (type(post_data),))
        url = model.pool.get('ir.config_parameter').get_param(cr, uid, 'url_ws.sice_orden_compras', context=context)
        if not url:
            raise Exception(u'No se encuentra configurada la conexión con SICE.\n \
                Ir a: Configuración -> Parámetros -> Parámetros del sistema y cargar un registro \
                con clave url_ws.sice_orden_compras y valor la URL del servicio web.')
        self.ensure_connection(url=url, msg_attr = 'Servicio: Orden Compra > Aprobar')
        _request = self._prepare_request_aprobar(post_data)
        #Response
        return self.client.service.aprobar(_request)
    #End Aprobar -------------------------------------------------------------------------------------------------

    #Begin Aprobar con Atributos -----------------------------------------------------------------------------------
    def _prepare_request_aprobar_attr(self, post_data):
        """
            @params post_data:
                {
                    See Documentation: Canal de Compras - Integración GRPs -v3.pdf. Page: 161
                }
        """
        return post_data

    def request_aprobar_attr(self, model, cr, uid, ids, post_data, context=None):
        """
            Método que ejecuta el servicio de orden compra: aprobar con atributos
            @see _prepare_request_aprobar_attr
        """
        if not isinstance(post_data, (dict,)):
            raise Exception("Se espera un diccionario como valor de retorno. Se ha recibido el tipo: %s" % (type(post_data),))
        url = model.pool.get('ir.config_parameter').get_param(cr, uid, 'url_ws.sice_orden_compras', context=context)
        if not url:
            raise Exception(u'No se encuentra configurada la conexión con SICE.\n \
                Ir a: Configuración -> Parámetros -> Parámetros del sistema y cargar un registro \
                con clave url_ws.sice_orden_compras y valor la URL del servicio web.')
        self.ensure_connection(url=url, msg_attr = 'Servicio: Orden Compra > Aprobar con Atributos')
        _request = self._prepare_request_aprobar_attr(post_data)
        #Response
        return self.client.service.aprobarConAtributos(_request)
    #End Aprobar con Atributos ------------------------------------------------------------------------------------------

    #Begin Cambiar Estado -----------------------------------------------------------------------------------------------
    def _prepare_request_cambiar_estado(self, post_data):
        """
            @params post_data:
                {
                    See Documentation: Canal de Compras - Integración GRPs -v3.pdf. Page: 162
                }
        """
        return post_data

    def request_cambiar_estado(self, model, cr, uid, ids, post_data, context=None):
        """
            Método que ejecuta el servicio de orden compra: cambiar estado
            @see _prepare_request_cambiar_estado
        """
        if not isinstance(post_data, (dict,)):
            raise Exception("Se espera un diccionario como valor de retorno. Se ha recibido el tipo: %s" % (type(post_data),))
        url = model.pool.get('ir.config_parameter').get_param(cr, uid, 'url_ws.sice_orden_compras', context=context)
        if not url:
            raise Exception(u'No se encuentra configurada la conexión con SICE.\n \
                Ir a: Configuración -> Parámetros -> Parámetros del sistema y cargar un registro \
                con clave url_ws.sice_orden_compras y valor la URL del servicio web.')
        self.ensure_connection(url=url, msg_attr = 'Servicio: Orden Compra > Cambiar Estado')
        _request = self._prepare_request_cambiar_estado(post_data)
        #Response
        return self.client.service.cambiarEstado(_request)
    #End Cambiar Estado --------------------------------------------------------------------------------------------------

    #Begin Cambiar Estado con Atributos ----------------------------------------------------------------------------------
    def _prepare_request_cambiar_estado_attr(self, post_data):
        """
            @params post_data:
                {
                    See Documentation: Canal de Compras - Integración GRPs -v3.pdf. Page: 162
                }
        """
        return post_data

    def request_cambiar_estado_attr(self, model, cr, uid, ids, post_data, context=None):
        """
            Método que ejecuta el servicio de orden compra: cambiar estado con atributos
            @see _prepare_request_cambiar_estado_attr
        """
        if not isinstance(post_data, (dict,)):
            raise Exception("Se espera un diccionario como valor de retorno. Se ha recibido el tipo: %s" % (type(post_data),))
        url = model.pool.get('ir.config_parameter').get_param(cr, uid, 'url_ws.sice_orden_compras', context=context)
        if not url:
            raise Exception(u'No se encuentra configurada la conexión con SICE.\n \
                Ir a: Configuración -> Parámetros -> Parámetros del sistema y cargar un registro \
                con clave url_ws.sice_orden_compras y valor la URL del servicio web.')
        self.ensure_connection(url=url, msg_attr = 'Servicio: Orden Compra > Cambiar Estado con Atributos')
        _request = self._prepare_request_cambiar_estado_attr(post_data)
        #Response
        return self.client.service.cambiarEstadoConAtributos(_request)
    #End Cambiar Estado con Atributos ----------------------------------------------------------------------------------------

    #Begin Consultar ---------------------------------------------------------------------------------------------------------
    def _prepare_request_consultar(self, post_data):
        """
            @params post_data:
                {
                    See Documentation: Canal de Compras - Integración GRPs -v3.pdf. Page: 162
                }
        """
        return post_data

    def request_consultar(self, model, cr, uid, ids, post_data, context=None):
        """
            Método que ejecuta el servicio de orden compra: consultar
            @see _prepare_request_consultar
        """
        if not isinstance(post_data, (dict,)):
            raise Exception("Se espera un diccionario como valor de retorno. Se ha recibido el tipo: %s" % (type(post_data),))
        url = model.pool.get('ir.config_parameter').get_param(cr, uid, 'url_ws.sice_orden_compras', context=context)
        if not url:
            raise Exception(u'No se encuentra configurada la conexión con SICE.\n \
                Ir a: Configuración -> Parámetros -> Parámetros del sistema y cargar un registro \
                con clave url_ws.sice_orden_compras y valor la URL del servicio web.')
        self.ensure_connection(url=url, msg_attr = 'Servicio: Orden Compra > Consultar')
        _request = self._prepare_request_consultar(post_data)
        #Response
        return self.client.service.consultar(_request)
    #End Consultar -------------------------------------------------------------------------------------------------------------

    #Begin Consultar con Atributos ---------------------------------------------------------------------------------------------
    def _prepare_request_consultar_attr(self, post_data):
        """
            @params post_data:
                {
                    See Documentation: Canal de Compras - Integración GRPs -v3.pdf. Page: 163
                }
        """
        return post_data

    def request_consultar_attr(self, model, cr, uid, ids, post_data, context=None):
        """
            Método que ejecuta el servicio de orden compra: consultar con atributos
            @see _prepare_request_consultar_attr
        """
        if not isinstance(post_data, (dict,)):
            raise Exception("Se espera un diccionario como valor de retorno. Se ha recibido el tipo: %s" % (type(post_data),))
        url = model.pool.get('ir.config_parameter').get_param(cr, uid, 'url_ws.sice_orden_compras', context=context)
        if not url:
            raise Exception(u'No se encuentra configurada la conexión con SICE.\n \
                Ir a: Configuración -> Parámetros -> Parámetros del sistema y cargar un registro \
                con clave url_ws.sice_orden_compras y valor la URL del servicio web.')
        self.ensure_connection(url=url, msg_attr = 'Servicio: Orden Compra > Consultar con Atributos')
        _request = self._prepare_request_consultar_attr(post_data)
        #Response
        return self.client.service.consultarConAtributos(_request)
    #End Consultar con Atributos -----------------------------------------------------------------------------------------------

    #Begin Listar --------------------------------------------------------------------------------------------------------------
    def _prepare_request_listar(self, post_data):
        """
            @params post_data:
                {
                    See Documentation: Canal de Compras - Integración GRPs -v3.pdf. Page: 163
                }
        """
        return post_data

    def request_listar(self, model, cr, uid, ids, post_data, context=None):
        """
            Método que ejecuta el servicio de orden compra: listar
            @see _prepare_request_listar
        """
        if not isinstance(post_data, (dict,)):
            raise Exception("Se espera un diccionario como valor de retorno. Se ha recibido el tipo: %s" % (type(post_data),))
        url = model.pool.get('ir.config_parameter').get_param(cr, uid, 'url_ws.sice_orden_compras', context=context)
        if not url:
            raise Exception(u'No se encuentra configurada la conexión con SICE.\n \
                Ir a: Configuración -> Parámetros -> Parámetros del sistema y cargar un registro \
                con clave url_ws.sice_orden_compras y valor la URL del servicio web.')
        self.ensure_connection(url=url, msg_attr = 'Servicio: Orden Compra > Listar')
        _request = self._prepare_request_listar(post_data)
        #Response
        return self.client.service.listar(**_request)
    #End Listar ----------------------------------------------------------------------------------------------------------------