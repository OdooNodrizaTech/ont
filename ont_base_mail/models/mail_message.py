# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models

import logging
_logger = logging.getLogger(__name__)

class MailMessage(models.Model):
    _inherit = 'mail.message'

    body = fields.Html('Contents', default='', sanitize_style=False, strip_classes=True)
    duration = fields.Float(help='Duration in minutes and seconds')