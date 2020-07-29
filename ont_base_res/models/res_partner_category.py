# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ResPartnerCategory(models.Model):
    _inherit = 'res.partner.category'
    _order = 'position'

    position = fields.Integer(
        string='Position'
    )
