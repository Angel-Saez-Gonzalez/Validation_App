from odoo import models, fields, api

class convalidationsModel(models.Model):
    _name = 'validation_app.convalidations_model'
    _description = 'Convalidations Module'

    date = fields.Date("Date", Required = True)
    module_id = fields.Many2one("validation_app.module_model", "Module")
    student_id = fields.Many2one("validation_app.student_model", "Student")
    