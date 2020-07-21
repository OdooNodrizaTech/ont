# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class StockHistory(models.Model):
    _inherit = 'stock.history'

    product_type = fields.Selection(
        string='Product type',
        related='product_id.type'
    )