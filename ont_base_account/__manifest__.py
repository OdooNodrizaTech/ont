# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Ont Base Account',
    'version': '10.0.1.0.0',    
    'author': 'Odoo Nodriza Tech (ONT)',
    'website': 'https://nodrizatech.com/',
    'category': 'Tools',
    'license': 'AGPL-3',
    'depends': ['base', 'account', 'sale'],
    'data': [
        'views/account_asset_asset.xml',
        'views/account_fiscal_position.xml',
        'views/account_invoice.xml',
        'views/account_move.xml',
        'views/account_move_line.xml',
        'views/account_payment_mode.xml',
        'views/account_payment_term.xml',
        'views/sale_order.xml',
    ],
    'installable': True,
    'auto_install': False,    
}