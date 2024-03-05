# Copyright 2024 Alberto Rodriguez - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import string
from odoo import fields, models


class AlfinfTrace(models.Model):
    _inherit = 'alfinf.trace'

    tz_ciclo = fields.Char(
        string='Ciclo'
    )
    tz_activa = fields.Char(
        string='Activa'
    )

    recinto_id = fields.Many2one(
        string='Recinto',
        comodel_name='alfinf.recinto',
        inverse_name='trace_ids'
    )
