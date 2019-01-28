# -*- coding: utf-8 -*-
from odoo import http

# class Shiftmanagement(http.Controller):
#     @http.route('/shiftmanagement/shiftmanagement/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/shiftmanagement/shiftmanagement/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('shiftmanagement.listing', {
#             'root': '/shiftmanagement/shiftmanagement',
#             'objects': http.request.env['shiftmanagement.shiftmanagement'].search([]),
#         })

#     @http.route('/shiftmanagement/shiftmanagement/objects/<model("shiftmanagement.shiftmanagement"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('shiftmanagement.object', {
#             'object': obj
#         })