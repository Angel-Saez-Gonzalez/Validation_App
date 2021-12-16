from odoo import models, fields, api

class moduleModel(models.Model):
    _name = 'validation_app.module_model'
    _description = 'Module Model'

    name = fields.Char("Module Name", Required = True)
    description = fields.Html("Description", Required = True)
    hours = fields.Integer("Hours", Required = True)
    convalidations = fields.One2many("validation_app.convalidations_model","module_id", "Convalidations")
    course_id = fields.Many2one("validation_app.course_model", "Course")
    