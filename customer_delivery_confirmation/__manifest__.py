{
    'name': 'Customer Delivery Confirmation',
    'version': '1.0',
    'summary': 'Allows customers to confirm delivery via QR code or customer portal',
    'category': 'Inventory',
    'author': 'Kais Akram',
    'license': 'LGPL-3',
    'depends': ['stock', 'website', 'mail', 'web'],
    'data': [
        'views/stock_picking_view.xml',
        'views/confirmation_page.xml',
        'views/package_received_templates.xml',
        'reports/delivery_report.xml',
        'data/email_template.xml',
    ],
   'assets': {
    'web.assets_frontend': [
        'customer_delivery_confirmation/static/src/js/confirmation_page.js',
    ],
},

    'installable': True,
    'application': False,
}
