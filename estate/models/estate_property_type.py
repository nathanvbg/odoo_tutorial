from odoo import models, fields
from . import estate_property

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = "Building's type."

    name = fields.Char(required=True)