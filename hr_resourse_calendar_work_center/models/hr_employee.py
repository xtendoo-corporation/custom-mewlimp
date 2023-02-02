from odoo import fields, models, api


class ResourceCalendar(models.Model):
    _inherit = 'resource.calendar'

    @api.model
    def create(self, vals):
        employees = super(ResourceCalendar, self).create(vals)

        print("*"*80)
        print("create hr employee")
        print("*"*80)

        return employees

    def write(self, vals):
        res = super(ResourceCalendar, self).write(vals)

        print("*"*80)
        print("write hr employee")
        print("*"*80)

        for rec in self:
            work_centers = rec.attendance_ids.filtered(lambda x: x.work_center_id).mapped("work_center_id")

        if not work_centers:
            return res

        print("*" * 80)
        print("work_centers", work_centers)
        print("*" * 80)

        employees = self.env["hr.employee"].search([("resource_calendar_id", "=", self.id)])
        if not employees:
            return res

        print("*" * 80)
        print("employees", employees)
        print("*" * 80)

        users = employees.filtered(lambda x: x.user_id).mapped("user_id")
        if not users:
            return res

        print("*"*80)
        print("users", users)
        print("*"*80)

        return res

    def _get_work_center(self):
        for rec in self:
            work_centers = rec.attendance_ids.filtered(lambda x: x.work_center_id).mapped("work_center_id")
            print(work_centers)
        return work_centers

    def _get_calendar_users(self):
        employees = self.env["hr.employee"].search([("resource_calendar_id", "=", self.id)])
        if not employees:
            return
        return employees.filtered(lambda x: x.user_id).mapped("user_id")


# @api.model
    # def create(self, vals=None):
    #     print("*"*80)
    #     print("create resource calendar")
    #     print("*"*80)
    #
    #     super().create(vals)
    #
    #     users = self._get_calendar_users()
    #     if users:
    #         for rec in self:
    #             print(rec.attendance_ids.filtered(lambda x: x.work_center_id).mapped("work_center_id"))
    #
    #     print("*" * 80)
    #     print("no hay usuarios")
    #     print("*" * 80)
    #
    # def write(self, vals):
    #     print("*"*80)
    #     print("write resource calendar")
    #     print("*"*80)
    #
    #     super().write(vals)
    #
    #     self._get_calendar_users()
    #
    #     for rec in self:
    #         print(rec.attendance_ids.filtered(lambda x: x.work_center_id).mapped("work_center_id"))
    #
    # def _get_calendar_users(self):
    #     employees = self.env["hr.employee"].search([("resource_calendar_id", "=", self.id)])
    #     if not employees:
    #         return
    #
    #     return employees.filtered(lambda x: x.user_id).mapped("user_id")

