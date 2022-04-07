

"""
just for referene purpose  adding field by inherting and using it.

"""

from odoo import fields, models,_

class Bonus(models.Model):

    _inherit = "arun.test"

    bonus_category = fields.Selection([
    ('workmen', 'WORKMEN'),
    ('aftersales', 'AFTERSALES'),
    ('supervisor', 'SUPERVISOR'),
    ('officestaff', 'OFFICESTAFF'),

    ], string="Bonus Category")