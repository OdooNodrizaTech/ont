# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, models, fields

import logging
_logger = logging.getLogger(__name__)

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    sale_order_note = fields.Text(
        string='Nota pedido de venta',
        related='sale_id.picking_note',
        store=False
    )
    purchase_id = fields.Many2one(
        comodel_name='purchase.order',
        string='Compra',
        copy=False
    )
    number_of_packages = fields.Integer(
        string='Bultos',
        default=1
    )
    number_of_pallets = fields.Integer(
        string='Palets',
        default=1
    )
    number_of_minipallets = fields.Integer(
        string='Minipalets',
        default=0
    )
    supplier_ref = fields.Char(
        string='Referencia del proveedor',
        size=30
    )
    partner_state_id = fields.Char(
        string='Provincia',
        related='partner_id.state_id.name',
        store=False
    )
    user_id_done = fields.Many2one(
        comodel_name='res.users',
        string='Preparado por',
        copy=False
    )
    management_date = fields.Datetime(
        string='Fecha preparacion',
        copy=False,
        readonly=True
    )

    @api.multi
    def _create_backorder(self, backorder_moves=[]):
        for obj in self:
            if obj.state == 'done' and obj.user_id_done.id == 0:
                obj.user_id_done = obj.env.uid  # Id actual
        # return
        return super(StockPicking, self)._create_backorder(backorder_moves)

    @api.multi
    def _add_delivery_cost_to_so(self):
        for obj in self:
            if obj.sale_id.id > 0:
                if obj.carrier_id.id > 0:
                    obj.sale_id.carrier_id = obj.carrier_id.id
        # return
        return super(StockPicking, self)._add_delivery_cost_to_so()