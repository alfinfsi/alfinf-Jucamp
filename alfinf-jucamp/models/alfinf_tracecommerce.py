# Copyright 2024 Pablo Martín - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import string
from odoo import fields, models


class AlfinfTraceCommerce(models.Model):
    _name = 'alfinf.tracecommerce'
    _description = 'Trazas para el control de gastos de comercio.'

    traza = fields.Char(
        string='Codigo de traza commerce',
    )

    finca_id = fields.Many2one(
        string='Finca',
        comodel_name='alfinf.finca',
        inverse_name='tracecommerce_ids'
    )
