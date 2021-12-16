# -*- coding: utf-8 -*-
# from odoo import http


# class ValidationApp(http.Controller):
#     @http.route('/validation_app/validation_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/validation_app/validation_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('validation_app.listing', {
#             'root': '/validation_app/validation_app',
#             'objects': http.request.env['validation_app.validation_app'].search([]),
#         })

#     @http.route('/validation_app/validation_app/objects/<model("validation_app.validation_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('validation_app.object', {
#             'object': obj
#         })
