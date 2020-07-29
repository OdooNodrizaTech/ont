# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class AccountPaymentMode(models.Model):
    _inherit = 'account.payment.mode'
    _order = 'position'

    position = fields.Integer(
        string='Position'
    )
    show_payment_method_id_journal_ids_in_pdf = fields.Boolean(
        string='Show in pdf',
        help='Show the account numbers of the newspapers of the '
             'linked payment method in the PDFs (Budget and Invoice)',
        default=False
    )
