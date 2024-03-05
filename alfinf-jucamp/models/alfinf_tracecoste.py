# Copyright 2024 Pablo Martín - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import string
from odoo import fields, models


class AlfinfTraceCoste(models.Model):
    _name = 'alfinf.tracecoste'
    _description = 'Trazas para el control de gastos de coste.'
    _rec_name='traza'

    traza = fields.Char(
        string='Codigo de traza commerce',
    )
    recinto_id = fields.Many2one(
        string='Recinto',
        comodel_name='alfinf.recinto',
        inverse_name='tracecoste_ids'
    )

