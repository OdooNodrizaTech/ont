# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class AccountPaymentTerm(models.Model):
    _inherit = 'account.payment.term'
    _order = 'position'
    
    position = fields.Integer(
        string='Position'
    )
    payment_order_ok = fields.Boolean(
        string='Selectable in orders'
    )
    payment_mode_id = fields.Many2many(
        comodel_name='account.payment.mode', 
        string='Payment modes',
    )
