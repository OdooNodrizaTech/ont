# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Ont Base Picking",
    "version": "12.0.1.0.0",
    "author": "Odoo Nodriza Tech (ONT), "
              "Odoo Community Association (OCA)",
    "website": "https://nodrizatech.com/",
    "category": "Tools",
    "license": "AGPL-3",
    "depends": [
        "base",
        "stock",
        "delivery",
        "sale",
        "purchase",
        "sale_stock"
    ],
    "data": [
        "views/sale_order_view.xml",
        "views/stock_picking_view.xml",
    ],
    "installable": True
}
