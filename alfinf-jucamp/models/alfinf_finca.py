# Copyright 2024 Pablo Martín - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import string
from odoo import fields, models

class AlfinfFinca(models.Model):
    _inherit = 'alfinf.finca'

    tracecommerce_ids = fields.One2many(
        string='Trazas en esta finca',
        comodel_name='alfinf.tracecommerce',
        inverse_name='finca_id'
    )
