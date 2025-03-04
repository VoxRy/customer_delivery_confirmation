from odoo import http
from odoo.http import request

class PackageReceiptController(http.Controller):

    @http.route('/confirm_receipt/<int:picking_id>', type='http', auth="public", website=True)
    def confirm_receipt(self, picking_id, **kwargs):
        picking = request.env['stock.picking'].sudo().browse(picking_id)

        # If picking does not exist, show 404 page
        if not picking.exists():
            return request.render('website.404')

        # Check if package is already confirmed
        if picking.package_received:
            return request.render('customer_delivery_confirmation.confirmation_success')

        # If not confirmed, show the form
        return request.render('customer_delivery_confirmation.confirmation_page', {'picking': picking})

    @http.route('/submit_package_received', type='http', auth="public", methods=['POST'], website=True)
    def submit_package_received(self, **post):
        picking_id = int(post.get('picking_id'))
        customer_name = post.get('customer_name')

        picking = request.env['stock.picking'].sudo().browse(picking_id)

        if picking.exists() and not picking.package_received:
            picking.sudo().action_confirm_receipt(customer_name)

        return request.render('customer_delivery_confirmation.confirmation_success')
