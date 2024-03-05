# Copyright 2024 Pablo Martín - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import string
from odoo import fields, models

class AlfinfFinca(models.Model):
    _inherit = 'alfinf.finca'

    #variedad_id = fields.One2many(
    #    string='Variedad',
    #    comodel_name='alfinf.variedad',
    #    inverse_name='finca_id'
    #)
