# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'


    work_center_partner_ids = fields.Many2many(
        comodel_name="res.partner",
    )
