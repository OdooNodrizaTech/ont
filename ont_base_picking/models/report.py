# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from openerp import api, models, fields
from openerp.exceptions import Warning
from datetime import datetime

import logging
_logger = logging.getLogger(__name__)

class Report(models.Model):
    _inherit = 'report'

    @api.multi
    def render(self, template, values=None):
        if template == "stock.report_deliveryslip":
            for doc in values['docs']:
                if doc.management_date == False:
                    doc.management_date = datetime.today()

        return super(Report, self).render(template, values)