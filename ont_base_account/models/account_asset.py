# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging
from odoo import api, models, fields


class AccountAsset(models.Model):
    _inherit = 'account.asset'
    
    depreciated_value = fields.Float(
        compute='_depreciated_value',
        string='Depreciated value',
        store=False
    )
    
    @api.one        
    def _depreciated_value(self):
        self.depreciated_value = 0
        if self.depreciation_line_ids:
            for depreciation_line_id in self.depreciation_line_ids:
                if depreciation_line_id.move_id:
                    if depreciation_line_id.move_id.state == 'posted':
                        self.depreciated_value += depreciation_line_id.amount
              
    @api.multi
    def set_to_close(self):
        for item in self:
            if item.state != 'close':
                if item.depreciation_line_ids:
                    for depreciation_line_id in item.depreciation_line_ids:
                        if item.state != 'close':
                            depreciation_line_id.post_lines_and_close_asset()                
            
        return super(AccountAssetAsset, self).set_to_close()

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
