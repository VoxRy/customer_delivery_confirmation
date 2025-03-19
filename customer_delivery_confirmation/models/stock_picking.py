import qrcode
import base64
from io import BytesIO
from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    # Teslimat onayı için alanlar
    package_received = fields.Boolean(string="Confirmed Receipt by Customer", default=False)
    package_received_date = fields.Datetime(string="Package Received At", readonly=True)
    customer_name = fields.Char(string="Customer Name", help="Name of the person who confirmed receipt")
    
    # QR kodu alanı
    qr_code = fields.Binary("QR Code", compute="_generate_qr_code", store=True)

    # Teslimat onayını işaretleyen fonksiyon
    def action_confirm_receipt(self, customer_name):
        """ Package received confirmation by the customer and store confirmation time """
        for picking in self:
            picking.sudo().write({
                'package_received': True,
                'package_received_date': fields.Datetime.now(),
                'customer_name': customer_name
            })
        return True

    @api.depends('name', 'package_received')
    def _generate_qr_code(self):
        """ Generate a QR code for package receipt confirmation """
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        for picking in self:
            if not picking.name:
                continue  # Eğer transfer adı yoksa, QR kodu oluşturma

            # QR kodu için URL oluşturma
            qr_url = f"{base_url}/confirm_receipt/{picking.id}"
            qr = qrcode.make(qr_url)  # QR kodunu oluştur
            qr_bytes = BytesIO()
            qr.save(qr_bytes, format="PNG")  # QR kodunu byte formatında kaydet

            # QR kodunu Base64 ile kodlayarak binary alana atama
            picking.qr_code = base64.b64encode(qr_bytes.getvalue())
    
    # QR kodunu manuel olarak oluşturacak bir buton fonksiyonu ekleme
    def action_generate_qr_code(self):
        """ Buton tıklandığında QR kodunu manuel olarak oluştur """
        for picking in self:
            if picking.name:
                base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
                qr_url = f"{base_url}/confirm_receipt/{picking.id}"
                qr = qrcode.make(qr_url)
                qr_bytes = BytesIO()
                qr.save(qr_bytes, format="PNG")
                picking.qr_code = base64.b64encode(qr_bytes.getvalue())
