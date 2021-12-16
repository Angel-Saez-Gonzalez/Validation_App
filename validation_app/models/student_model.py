from odoo import models, fields, api
import random
import string

class studentModel(models.Model):
    _name = 'validation_app.student_model'
    _description = 'Validation Model'

    name = fields.Char("Student Name", Required = True)
    password = fields.Char("Password", Required = True)
    photo = fields.Binary("Photo")
    age = fields.Integer("Age", Required = True)
    ageMinor = fields.Integer("Minor")
    locality = fields.Char("Locality", Required = True)
    province = fields.Char("Province", Required = True)
    email = fields.Char("Email", Required = True)
    convalidations = fields.One2many("validation_app.convalidations_model","student_id", "Convalidations")

    def generatePassword(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(8))
        self.password = password

    def minor(self):
        if self.age < 18:
            self.ageMinor = self.age
