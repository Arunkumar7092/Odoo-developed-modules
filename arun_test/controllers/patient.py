from odoo import http
from odoo.http import request
import logging
import base64
from base64 import b64encode
import werkzeug
import json
import pytz
import time
import pdb
import datetime as mydatetime
from openerp.addons.web.controllers.main import serialize_exception,content_disposition

from collections import OrderedDict,defaultdict, Counter
from calendar import monthrange
from datetime import datetime, timedelta, date
from odoo.addons.website.controllers.main import Website
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT,\
    DEFAULT_SERVER_DATE_FORMAT
from odoo.tools.translate import _


_logger = logging.getLogger(__name__)


class CustomerController(http.Controller):
    @http.route('/patients', type='http', auth='user',methods=['POST'], website=True, csrf=False)
    def render_customer_page(self, **post):
        search_data = post.get('search')
        res_obj = request.env['arun.test']
        final_data ={}
        details=[]
        res_id = res_obj.sudo().search(['|' ,'|' ,'|' ,('test_name','ilike',search_data),
                                        ('test_age','ilike',search_data),
                                        ('email_id','ilike',search_data),
                                        ('name_seq','ilike',search_data)])
        
        if res_id:
            for res in res_id:
                arRy={}
                res_obj = (res)
                arRy["partner_id"] = res_obj.id
                arRy["test_arun"] = res_obj.test_name
                arRy["test_age"] = res_obj.test_age
                arRy["company_name"] = res_obj.company_name
                arRy["pan_no"] = res_obj.pan_no
                arRy["aadhar_no"] = res_obj.aadhar_no
                arRy["email_id"] = res_obj.email_id
                
                details.append(arRy)
            final_data["details"] = details
            print("Answer of details",details)
            return http.request.render("arun_test.customer_page", final_data)
        else:
            return http.request.render('arun_test.NewPatientProfile', {'data':search_data})
    
    @http.route('/create-patient', type="http",auth="public", website=True, csrf=False)
    def createpatient_page(self,**post):
        return http.request.render('arun_test.CreatePatient', {})
    


    @http.route('/patient-created', type="http",methods=['POST'], auth="public", website=True)
    def create_webpatient(self, **post):
        print("Data Received.....", post)


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
            'sc_To3':post.get('sc_To3')
        }
                                    

        print(">>>>>>>>>>>these is val",val)

        rec = request.env['arun.test'].sudo().create(val)
        return request.render("arun_test.employee_thanks", {})

 
