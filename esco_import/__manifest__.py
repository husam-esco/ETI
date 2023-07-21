{
    'name': 'ESCO Sales Import',
    'version': '0.0.1',
    'summary': 'This module is used to upload xls files and create a sale order query from it',
    'description': 'This module is used to upload xls files and create a sale order query from it',
    'category': 'Sales',
    'author': 'Engineering Solutions Company',
    'website': 'escoiq.com',
    'license': 'LGPL-3',
    'depends': ['base', 'sale', 'stock', 'sale_order_automation'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        #'security/security.xml',
        'views/views.xml',
    ],
    'demo': ['Demo'],
    'installable': True,
    'auto_install': False
}
