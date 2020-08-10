# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging
from odoo import models, _
_logger = logging.getLogger(__name__)


class TrialBalanceXslx(models.AbstractModel):
    _inherit = 'report.a_f_r.report_trial_balance_xlsx'

    def _get_report_columns(self, report):
        content = super(TrialBalanceXslx, self)._get_report_columns(report)
        if not report.show_partner_details:
            content_new = {
                0: content[0],
                1: content[1],
                # add_new_fields
                2: {
                    'header': _("Type"),
                    'field': 'custom_type',
                    'type': 'selection',
                    'width': 7
                },
                3: {
                    'header': _("Clasification"),
                    'field': 'custom_classification',
                    'width': 7
                }
            }
            content_new[1]['width'] = 46
            for content_key in content:
                if content_key >= 2:
                    content_new[len(content_new)] = content[content_key]
            # end
            content = content_new

        return content
