# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models, fields


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    inv_vat = fields.Char(
        string='VAT',
        related='partner_id.vat'
    )
    partner_bank_name = fields.Char(
        compute='_compute_partner_bank_name',
        string='Bank name'
    )

    @api.multi
    @api.depends('partner_bank_id')
    def _compute_partner_bank_name(self):
        self.ensure_one()
        self.partner_bank_name = ''
        if self.partner_bank_id:
            if self.partner_bank_id.bank_id:
                self.partner_bank_name = "%s %s" % (
                    self.partner_bank_id.bank_id.name,
                    self.partner_bank_id.acc_number[-4:]
                )
            else:
                self.partner_bank_name = self.partner_bank_id.acc_number
