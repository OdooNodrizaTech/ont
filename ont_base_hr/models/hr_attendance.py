# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models

import logging
_logger = logging.getLogger(__name__)

class HrAttendance(models.Model):
    _inherit = 'hr.attendance'    
    
    @api.model
    def create(self, values):
        allow_create = True
        # check multiple attendance without check_out
        if 'check_out' not in values:
            hr_attendance_ids = self.env['hr.attendance'].sudo().search(
                [
                    ('employee_id', '=', values['employee_id']),
                    ('check_out', '=', False)
                ]
            )
            if hr_attendance_ids:
                allow_create = False
        
        if allow_create:
            return_create = super(HrAttendance, self).create(values)
            return return_create                              