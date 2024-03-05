# Copyright 2024 Pablo Martín - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import string
from odoo import fields, models

class AlfinfVariedad(models.Model):
    _inherit= 'alfinf.variedad'

    tracecommerce_ids = fields.Many2one(
        string='Tracecommerce',
        comodel_name='alfinf.tracecommerce',
        inverse_name='variedad_id'
    )
    recinto_ids = fields.One2many(
        string='Recintos',
        comodel_name='alfinf.recinto',
        inverse_name='variedad_id'
    )
