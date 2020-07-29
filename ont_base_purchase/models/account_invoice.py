# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.onchange('purchase_id')
    def purchase_order_change(self):
        if self.purchase_id:
            purchase_id = self.purchase_id
            
            return_val = super(AccountInvoice, self).purchase_order_change()
                    
            if purchase_id.user_id:
                self.user_id = purchase_id.user_id.id
                
            if purchase_id.payment_mode_id:
                self.payment_mode_id = purchase_id.payment_mode_id.id
                
        return {}
