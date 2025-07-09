{
    'name': 'Customer Delivery Confirmation',
    'version': '1.0',
    'summary': 'Allows customers to confirm delivery via QR code or customer portal',
    'category': 'Inventory',
    'author': 'Kais Akram',
    'license': 'LGPL-3',
    'website': 'https://yourcompany.com',
    'depends': ['stock', 'website', 'mail', 'web'],
    'data': [
        'views/stock_picking_view.xml',
        'views/confirmation_page.xml',
        'views/package_received_templates.xml',
        'reports/delivery_report.xml',
        'reports/qr_delivery_report.xml',  # ✅ Yeni rapor eklendi
        'data/email_template.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'customer_delivery_confirmation/static/src/js/confirmation_page.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'description': """
Customer Delivery Confirmation via QR Code

This module allows customers to confirm the receipt of delivery orders by scanning a QR code or visiting a confirmation portal. 
The module generates a QR code on delivery orders, includes legal consent checkboxes, and provides a backend view of confirmations.

Features:
- QR code on delivery slip
- Public confirmation form
- KVKK and consent approval
- Backend fields showing confirmation status
- Manual QR generation & print

Author: Kais Akram
    """,
}
