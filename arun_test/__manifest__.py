{
    'name':'Employee Hiring',
    'version': '14.0.1.0.0',
    'author': 'Arun',
    'summary': "testing pupose system",
    'sequence': -1,
    'description':"This is Arun krish demo testing module in "
                  "Odoo v14",
    'category':'Testing',
    'website':'https://Arunkrish.blogspot.com',
    'depends':['base','mail','website',],
    'data':[
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/test_view.xml",
        "views/employee_contacts.xml",
        "views/template.xml",
        "views/template2.xml",
        "views/template3.xml",
        "views/pos_chatter.xml",
        "views/customer_page_template.xml",
        "views/new_patient_profile.xml",
        "views/create_new_patient.xml",
        "views/employee_thanks.xml",


        "reports/employee_details.xml",
        "reports/report.xml",
        "reports/employee_appointment_letter.xml",
        "reports/employee_resume.xml",

        # "reports/report_resume_format.xml",



        

    ],
    'installable': True,
    'Application': True,
    'auto installation':False,

}
