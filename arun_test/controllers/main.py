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

class employee(http.Controller):

    @http.route('/employee_webform', type="http", auth="public", website=True)
    def patient_webform(self, **kw):
        print("Execution Here.........................")
        print("test1...")
        return http.request.render('arun_test.create_employee', {
                                                                })

    @http.route('/create/webemployee', type="http",methods=['POST'], auth="public", website=True)
    def create_webpatient(self, **post):
        print("Data Received.....", post)

        x = 1
        employee_rec = []
        count = post.get('countexp')
        for i in range(0,int(count)):
        # for i,j in post.items():
            print("before3",x)
            print("count ex",i)

            # if 'empployment_name'+str(x) in post and 'employment_id'+str(x) in post and 'empployment_title'+str(x) in post and 'from_date'+str(x) in post and 'To_date'+str(x) in post and 'employment_salary'+str(x) in post and 'employment_resignation'+str(x) in post and 'empployment_address'+str(x) in post:
            #     if post.get('empployment_name'+str(x))=='' and post.get('employment_id'+str(x))=='' and post.get('empployment_title'+str(x))=='' and post.get('from_date'+str(x))=='' and post.get('To_date'+str(x))=='' and post.get('employment_salary'+str(x))==''and post.get('employment_resignation'+str(x))=='' and post.get('empployment_address'+str(x))=='':
            #         employee_rec = False
            # else:
            print("else down",post.get('empployment_name'+str(x)))
            employee_rec.append((0, 0, {'empployment_name':post.get('empployment_name'+str(x)),
                            'employment_id':post.get('employment_id'+str(x)),
                            'empployment_title':post.get('empployment_title'+str(x)),
                            'from_date':post.get('from_date'+str(x)),
                            'To_date':post.get('To_date'+str(x)),
                            'employment_salary':post.get('employment_salary'+str(x)),
                            'employment_resignation':post.get('employment_resignation'+str(x)),
                            'empployment_address':post.get('empployment_address'+str(x))}))
            x=x+1
            print("after3",x)

        
        s = 1
        skill_rec = []
        count = post.get('countskl')
        print("..................................count",count)
        for i in range(0,int(count)):
        # for i,j in post.items():
            print("skill_rec s value",s)
            print("skill rec i value",i)

            # if 'empployment_name'+str(x) in post and 'employment_id'+str(x) in post and 'empployment_title'+str(x) in post and 'from_date'+str(x) in post and 'To_date'+str(x) in post and 'employment_salary'+str(x) in post and 'employment_resignation'+str(x) in post and 'empployment_address'+str(x) in post:
            #     if post.get('empployment_name'+str(x))=='' and post.get('employment_id'+str(x))=='' and post.get('empployment_title'+str(x))=='' and post.get('from_date'+str(x))=='' and post.get('To_date'+str(x))=='' and post.get('employment_salary'+str(x))==''and post.get('employment_resignation'+str(x))=='' and post.get('empployment_address'+str(x))=='':
            #         employee_rec = False
            # else:
            print("else down",post.get('employee_skills'+str(s)))
            skill_rec.append((0, 0, {'employee_skills':post.get('employee_skills'+str(s))}))
            s=s+1
            print("after",s)
        
        l = 1
        lang_rec = []
        count = post.get('countlan')
        print("..................................count",count)
        for i in range(0,int(count)):
            lang_rec.append((0, 0, {'language':post.get('language'+str(l))}))
            l=l+1


        val = {
            'test_name':post.get('test_name'),
            'test_age':post.get('test_age'),
            'job_position':post.get('job_position'),
            'email_id':post.get('email_id'),
            'start_date':post.get('start_date'),
            'company_name':post.get('company_name'),
            'inst_owner':post.get('inst_owner'),
            'about':post.get('about'),
            'school':post.get('school'),
            'sc_percentage':post.get('sc_percentage'),
            'rollno1':post.get('rollno1'),
            'sc_From1':post.get('sc_From1'),
            'sc_To1':post.get('sc_To1'),
            'school2':post.get('school2'),
            'sc_percentage2':post.get('sc_percentage2'),
            'rollno2':post.get('rollno2'),
            'sc_From2':post.get('sc_From2'),
            'sc_To2':post.get('sc_To2'),
            'college_name':post.get('college_name'),
            'dg_percentage':post.get('dg_percentage'),
            'rollno3':post.get('rollno3'),
            'degree':post.get('degree'),
            'sc_From3':post.get('sc_From3'),
            'sc_To3':post.get('sc_To3'),
            

            'employment_line_ids':employee_rec,
            'language_speak':lang_rec,
            'skills':skill_rec
        }
        print("answeer",employee_rec)
        print(">>>>>>>>>>>these is val",val)

        rec = request.env['arun.test'].sudo().create(val)
        # print("<><><><><><>",rec)
        return request.render("arun_test.employee_thanks", {})


