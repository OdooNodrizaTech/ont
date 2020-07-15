# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging
_logger = logging.getLogger(__name__)

from openerp import api, models, fields
from openerp.exceptions import Warning

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'
    
    @api.onchange('purchase_id')
    def purchase_order_change(self):
        if self.purchase_id.id>0:        
            purchase_id = self.purchase_id
            
            return_val = super(AccountInvoice, self).purchase_order_change()
                    
            if purchase_id.user_id.id>0:
                self.user_id = purchase_id.user_id.id
                
            if purchase_id.payment_mode_id.id>0:
                self.payment_mode_id = purchase_id.payment_mode_id.id              
                
        return {}