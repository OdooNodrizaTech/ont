# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, models, _
from odoo.exceptions import Warning as UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def action_confirm(self):
        allow_confirm = True
        # check
        for item in self:
            if item.amount_total > 0:
                if not item.partner_invoice_id.vat:
                    allow_confirm = False
                    raise UserError(_("It is necessary to define "
                                      "the VAT for the billing "
                                      "address before validating "
                                      "the sales order"))
        # allow_confirm
        if allow_confirm:
            return super(SaleOrder, self).action_confirm()
