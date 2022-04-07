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

class education(http.Controller):

    @http.route('/employee_educationform', type="http", auth="public", website=True)
    def education_webform(self, **kw):
        print("Execution Here.........................")
        # doctor_rec = request.env['hospital.doctor'].sudo().search([])
        print("test1...")
        return http.request.render('arun_test.create_educational', {
                                                                })

    @http.route('/create/webeducation', type="http", auth="public", website=True)
    def create_webpatient(self, **kw):
        print("Data Received.....", kw)
        request.env['arun.test'].sudo().create(kw)
        return request.render("arun_test.employee_thanks", {})
