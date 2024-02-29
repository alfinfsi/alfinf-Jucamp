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

    recinto_id = fields.Many2one(
        string='Parcela',
        comodel_name='alfinf.recinto',
        inverse_name='tracecommerce_ids'
    )

    #variedad_id = fields.One2many('alfinf.variedad', 'tracecommerce_id', string='Variedad')

    #@api.constrains('variedad_id')
    #def _check_unique_relation(self):
    #    for record in self:
    #        if len(record.variedad_id) > 1:
    #            raise ValidationError("Una dirección solo puede estar asociada a una traza.")
