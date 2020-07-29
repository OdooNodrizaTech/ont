# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models, _
from odoo.exceptions import Warning as UserError


class MailComposer(models.TransientModel):
    _inherit = 'mail.compose.message'

    @api.multi
    def check_limit_size_attachments(self):
        limit_size = 1000000*10
        item_size = 0
        for item in self:
            if item.attachment_ids:
                for attachment_id in item.attachment_ids:
                    item_size = item_size + attachment_id.file_size

            if item_size >= limit_size:
                raise UserError(_('The maximum limit of email attachments is 10MB'))

    @api.multi
    @api.onchange('attachment_ids', 'template_id')
    def onchange_attachment_ids(self):
        for item in self:
            item.check_limit_size_attachments()
