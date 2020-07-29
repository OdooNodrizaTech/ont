# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Ont Base Account",
    "version": "12.0.1.0.0",
    "author": "Odoo Nodriza Tech (ONT), "
              "Odoo Community Association (OCA)",
    "website": "https://nodrizatech.com/",
    "category": "Tools",
    "license": "AGPL-3",
    "depends": [
        "base",
        "account",
        "sale",
        "account_payment_mode",  # https://github.com/OCA/bank-payment
        "account_asset_management",  # https://github.com/OCA/account-financial-tools
        "crm_claim"  # https://github.com/OCA/crm
    ],
    "data": [
        "data/ir_cron.xml",
        "views/account_account_view.xml",
        "views/account_asset_view.xml",
        "views/account_fiscal_position_view.xml",
        "views/account_invoice_view.xml",
        "views/account_move_view.xml",
        "views/account_move_line_view.xml",
        "views/account_payment_mode_view.xml",
        "views/account_payment_term_view.xml",
        "views/sale_order_view.xml",
    ],
    "installable": True
}
