from odoo import fields, models, api


class ResourceCalendar(models.Model):
    _inherit = 'resource.calendar'

    @api.model
    def create(self, vals):
        res = super(ResourceCalendar, self).create(vals)
        for calendar in self:
            users = calendar._get_calendar_users(calendar)
            work_centers = calendar._get_calendar_work_center(calendar)
            for work_center in work_centers:
                work_center.work_center_user_ids = [(4, user.id) for user in users]
        return res

    def write(self, vals):
        res = super(ResourceCalendar, self).write(vals)
        for calendar in self:
            users = calendar._get_calendar_users(calendar)
            work_centers = calendar._get_calendar_work_center(calendar)
            for work_center in work_centers:
                work_center.work_center_user_ids = [(4, user.id) for user in users]
        return res

    def _get_calendar_work_center(self, calendar):
        return calendar.attendance_ids.filtered(lambda x: x.work_center_id).mapped("work_center_id")

    def _get_calendar_users(self, calendar):
        employees = self.env["hr.employee"].search([("resource_calendar_id", "=", calendar.id)])
        if not employees:
            return
        return employees.filtered(lambda x: x.user_id).mapped("user_id")


