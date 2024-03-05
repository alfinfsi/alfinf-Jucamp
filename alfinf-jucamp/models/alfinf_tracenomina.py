# Copyright 2024 Pablo Martín - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import string
from odoo import fields, models


class AlfinfTraceNomina(models.Model):
    _name = 'alfinf.tracenomina'
    _description = 'Trazas para el control de gastos de nominas.'
    _rec_name='traza'

    traza = fields.Char(
        string='Codigo de traza nominas',
    )

    parcela_id = fields.Many2one(
        string='Parcela',
        comodel_name='alfinf.parcela',
        inverse_name='tracenomina_ids'
    )
    recinto_id = fields.Many2one(
        string='Recinto',
        comodel_name='alfinf.recinto',
        inverse_name='tracenomina_ids'
    )

    #@api.constrains('variedad_id')
    #def _check_unique_relation(self):
    #    for record in self:
    #        if len(record.variedad_id) > 1:
    #            raise ValidationError("Una dirección solo puede estar asociada a una traza.")
