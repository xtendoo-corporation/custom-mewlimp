from odoo import api, models, _, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    work_center_user_ids = fields.Many2many(
        comodel_name="res.users",
        string="Users for work center",
    )
