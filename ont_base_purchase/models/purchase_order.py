# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging
_logger = logging.getLogger(__name__)

from openerp import api, models, fields
from openerp.exceptions import Warning

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
        
    payment_mode_id = fields.Many2one(
        comodel_name='account.payment.mode', 
        string='Forma de pago',
        index=True        
    )
    user_id = fields.Many2one(
        comodel_name='res.users', 
        string='Comercial',
        index=True,  
        default=lambda self: self.env.user
    )

    @api.multi
    def button_confirm(self):
        # action_confirm
        return_data = super(PurchaseOrder, self).button_confirm()
        #operations
        for item in self:
            if item.state=='purchase':
                for picking_id in item.picking_ids:
                    picking_id.purchase_id = item.id
        #return
        return return_data