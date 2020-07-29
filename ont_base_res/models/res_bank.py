# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ResBank(models.Model):
    _inherit = 'res.bank'

    public_name = fields.Char(
        string='Public name'
    )
