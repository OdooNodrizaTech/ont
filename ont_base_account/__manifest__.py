# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Ont Base Account",
    "version": "12.0.1.0.0",
    "author": "Odoo Nodriza Tech (ONT)",
    "website": "https://nodrizatech.com/",
    "category": "Tools",
    "license": "AGPL-3",
    "depends": [
        "base",
        "account",
        "sale",
        "account_asset_management"
    ],
    "data": [
        "data/ir_cron.xml",
        "views/account_asset_view.xml",
        "views/account_fiscal_position_view.xml",
        "views/account_invoice_view.xml",
        "views/account_move_view.xml",
        "views/account_move_line_view.xml",
        "views/account_payment_mode_view.xml",
        "views/account_payment_term_view.xml",
        "views/sale_order_view.xml",
    ],
    "installable": True,
}