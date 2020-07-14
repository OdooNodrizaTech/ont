# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging
_logger = logging.getLogger(__name__)

from openerp import api, models, fields
from openerp.exceptions import Warning

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    payment_mode_id = fields.Many2one(
        comodel_name='account.payment.mode', 
        string='Modo de pago',
    )

    @api.multi
    def action_confirm(self):
        allow_action_confirm = True
        for item in self:
            if item.amount_total > 0 and item.claim == False:
                payment_mode_ids_allow = []
                for payment_mode_id in item.payment_term_id.payment_mode_id:
                    payment_mode_ids_allow.append(payment_mode_id.id)

                if not item.payment_mode_id.id in payment_mode_ids_allow:
                    allow_action_confirm = False
                    raise Warning("El modo de pago es incompatible con el plazo de pago")

        if allow_action_confirm == True:
            return super(SaleOrder, self).action_confirm()