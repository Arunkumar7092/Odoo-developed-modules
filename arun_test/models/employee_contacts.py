from odoo import fields, models,api,_

class EmployeeContacts(models.Model):
    _name = "employee.contacts"
    _description = 'employee contacts'

    employee_name = fields.Many2one('arun.test', string = 'Name')
    mobile_num = fields.Char(string = "Mobile Number")
    email = fields.Char("Email")
    image = fields.Binary()


    # @api.depends('employee_name')
    # def get_mobile_number(self):
    #     for rec in self:
    #         if rec.employee_name:
    #             self.mobile_num = self.company_name


    @api.onchange('employee_name')
    def get_emp_mobile(self):
        if self.employee_name:
            self.mobile_num = self.employee_name.company_name
            self.email = self.employee_name.email_id
            self.image = self.employee_name.image
            


       