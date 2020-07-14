# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging
_logger = logging.getLogger(__name__)

from openerp import api, models, fields
from openerp.exceptions import Warning

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    @api.multi
    def action_confirm(self):
        allow_confirm = True
        #check
        for obj in self:
            if obj.amount_total>0:            
                if obj.partner_invoice_id.vat==False:
                    allow_confirm = False
                    raise Warning("Es necesario definir VAT para la direccion de facturacion antes de validar el pedido de venta.\n")                           
        #allow_confirm
        if allow_confirm==True:
            return super(SaleOrder, self).action_confirm()