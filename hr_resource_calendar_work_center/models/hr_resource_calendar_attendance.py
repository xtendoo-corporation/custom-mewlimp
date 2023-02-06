from odoo import models, fields, api, exceptions, _


class ResourceCalendarAttendance(models.Model):
    _inherit = "resource.calendar.attendance"


    work_center_id = fields.Many2one(
        comodel_name='res.partner',
        string="Work Center",
        domain="[('is_work_center', '=', True)]",
    )


