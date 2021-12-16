from odoo import models, fields, api

class courseModel(models.Model):
    _name = 'validation_app.course_model'
    _description = 'Course Module'

    name = fields.Char("Name", Required = True)
    description = fields.Html("Description")
    modules = fields.One2many("validation_app.module_model","course_id", "Modules")
    