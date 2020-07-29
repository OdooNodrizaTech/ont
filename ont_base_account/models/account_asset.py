# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models, fields


class AccountAsset(models.Model):
    _inherit = 'account.asset'

    depreciated_value = fields.Float(
        compute='_compute_depreciated_value',
        string='Depreciated value',
        store=False
    )

    @api.multi
    def _compute_depreciated_value(self):
        for item in self:
            item.depreciated_value = 0
            if item.depreciation_line_ids:
                for line_id in item.depreciation_line_ids:
                    if line_id.move_id:
                        if line_id.move_id.state == 'posted':
                            item.depreciated_value += line_id.amount

    @api.multi
    def set_to_close(self):
        for item in self:
            if item.state != 'close':
                if item.depreciation_line_ids:
                    for line_id in item.depreciation_line_ids:
                        if item.state != 'close':
                            line_id.post_lines_and_close_asset()

        return super(AccountAsset, self).set_to_close()

    @api.model
    def _cron_generate_entries(self):
        items = self.env['account.asset'].search(
            [
                ('state', '=', 'open')
            ]
        )
        created_move_ids, error_log = items._compute_entries(
            fields.Date.today(),
            check_triggers=True
        )
