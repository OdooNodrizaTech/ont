# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import models, fields, api


class TrialBalanceReportAccount(models.TransientModel):
    _inherit = 'report_trial_balance_qweb_account'

    custom_type = fields.Char(
        compute='_compute_custom_type',
        string='Type',
        store=False
    )
    custom_classification = fields.Char(
        compute='_compute_custom_classification',
        string='Clasification',
        store=False
    )

    @api.multi
    @api.depends('account_id')
    def _compute_custom_type(self):
        for item in self:
            if item.account_id:
                item.custom_type = dict(
                    item.account_id._fields['custom_type'].selection
                ).get(item.account_id.custom_type)

    @api.multi
    @api.depends('account_id')
    def _compute_custom_classification(self):
        for item in self:
            if item.account_id:
                item.custom_classification = dict(
                    item.account_id._fields['custom_classification'].selection
                ).get(item.account_id.custom_classification)