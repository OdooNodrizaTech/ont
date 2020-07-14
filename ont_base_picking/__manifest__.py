# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Ont Base Picking',
    'version': '12.0.1.0.0',    
    'author': 'Odoo Nodriza Tech (ONT)',
    'website': 'https://nodrizatech.com/',
    'category': 'Tools',
    'license': 'AGPL-3',
    'depends': ['base', 'stock', 'delivery', 'sale', 'purchase'],
    'data': [
        'views/sale_order.xml',
        'views/stock_picking.xml',
    ],
    'installable': True,
    'auto_install': False,    
}