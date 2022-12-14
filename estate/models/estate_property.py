from odoo import models, fields
from . import estate_property_type
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = "Properties in sale."

    active = fields.Boolean('Active', default=True)
    state = fields.Selection([
        ('New', 'New'),
        ('Offer Received', 'Offer Received'),
        ('Offer Accepted', 'Offer Accepted'),
        ('Sold','Sold'),
        ('Canceled', 'Canceled')], 'State', default='New', required=True, copy=False
    )
    name = fields.Char(required=True)
    description = fields.Char()
    postcode = fields.Char(help=None)
    date_availability = fields.Date(copy=False, default=lambda self: fields.Datetime.now() + relativedelta(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection=[('North', 'North'), ('South', 'South'), ('East', 'East'), ('West','West')]
    )
    estate_property_type_id = fields.Many2one("estate.property.type", string="Building's type")
    buyer_id = fields.Many2one("res.partner", string="Buyer's name")
    salesperson_id = fields.Many2one("res.users", string="seller's name", default=lambda self: self.env.user)
