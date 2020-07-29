# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models


class MailMessage(models.Model):
    _inherit = 'mail.message'

    body = fields.Html(
        string='Contents',
        default='',
        sanitize_style=False,
        strip_classes=True
    )
    duration = fields.Float(
        help='Duration in minutes and seconds'
    )
