# Copyright 2024 Pablo Martín - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import string
from odoo import fields, models

class AlfinfVivero(models.Model):
    _name = 'alfinf.vivero'

    name = fields.Char(
        string='Nombre dle vivero'
    )
