# Copyright 2024 Pablo Martín - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import string
from odoo import fields, models

class AlfinfRecinto(models.Model):
    _inherit = 'alfinf.recinto'

    tracecommerce_ids = fields.One2many(
        string='Trazas commerce en esta finca',
        comodel_name='alfinf.tracecommerce',
        inverse_name='recinto_id'
    )
    tracecommerce_ids = fields.Many2one(
        string='Tracecommerce',
        comodel_name='alfinf.tracecommerce',
        inverse_name='variedad_id'
    )
    #variedad_id = fields.One2many(
    #    string='Variedad',
    #    comodel_name='alfinf.variedad',
    #    inverse_name='finca_id'
    #)
