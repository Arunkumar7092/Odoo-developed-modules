from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


# class Employee(http.Controller):

#     @http.route('/employee/hiring/', website=True, auth='user')
#     def employee_hiring(self, **kw):
#         # return "Thanks for watching"
#         employees = request.env['arun.test'].sudo().search([])
#         # ages = request.env['arun.test'].sudo().search([])
#         return request.render("arun_test.employee_page", {
#             'employees': employees,
#             # 'ages': ages
#         })

class contact(http.Controller):

    @http.route('/employee_skillsetform', type="http", auth="public", website=True)
    def contact_webform(self, **kw):
        print("Execution Here.   3........................")
        test1 = request.env['employee.contacts'].sudo().search([])
        test = request.env['res.partner'].sudo().search([])
        print("test1...")
        return http.request.render('arun_test.create_employeecontacts', {'test1': test1 ,'test':test})
                                                                

    @http.route('/create/employeecontacts', type="http", auth="public", website=True)
    def create_webcontact(self, **kw):
        print("Data Received.....", kw)
        request.env['res.partner'].sudo().create(kw)
        return request.render("arun_test.employee_thanks", {})
