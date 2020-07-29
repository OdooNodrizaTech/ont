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
        for item in self:
            item.partner_bank_name = ''
            if item.partner_bank_id:
                if item.partner_bank_id.bank_id:
                    item.partner_bank_name = "%s %s" % (
                        item.partner_bank_id.bank_id.name,
                        item.partner_bank_id.acc_number[-4:]
                    )
                else:
                    item.partner_bank_name = item.partner_bank_id.acc_number
