from odoo import fields, models, api,_
from odoo.exceptions import ValidationError

class ArunTest(models.Model):
    _name = "arun.test"
    _description = 'arun test record'
    _rec_name ='test_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']




    # below is the function to change the status while clicking buttons  ,call those actions inside the button to change the status
    #1 BUTTON AND STATUS BAR SECTION#

    state = fields.Selection([
        ('initial','Initial Qualification'), 
        ('interview1','First Interview'), 
        ('interview2','Second Interview'),
        ('wait','waiting'), 
        ('Hire','Hired'), 
        ('reject','rejected'),
        ('cancel','cancelled')
        ],string="status")



    def action_interview1(self):
        self.state = "interview1"
    

    def action_interview2(self):
        self.state = "interview2"



    def action_hire(self):
        self.state = "Hire"

    def action_wait(self):
        self.state = "wait"
    

    def action_reject(self):
        self.state = "reject"

    def action_cancel(self):
        self.state = "cancel"


    # order reference number geneartion #
    # _rec_name ='test_name'
    #related file is /data/sequence.xml and test_view.xml


    name_seq=fields.Char(string='Order Reference', required = True, copy = False, readonly = True, index = True, default = lambda self:_('New'))

    @api.model
    def create(self,vals):
        if vals.get('name_seq',_('New'))==_('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('employee.details.sequence') or _('New')
        result=super(ArunTest,self).create(vals)
        return result

    image = fields.Binary()




    
    employee_name = fields.Char("Name")
    mobile_num = fields.Char("Mobile Number")
    email = fields.Char("Email")


    test_name = fields.Char(string="Name",track_visibility ="always")
    test_age = fields.Integer('age',track_visibility ="always")
    notes = fields.Text(string="Description")
    college_name = fields.Char('college Name')
    company_name = fields.Char('Mobile Number')
    inst_owner = fields.Char('Contact address')
    start_date = fields.Date('Birth Date')
    # end_date = fields.Date('End Date')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], default='male', string="Gender")

    
    rollno1 = fields.Char('Registration number')
    rollno2 = fields.Char('Registration number')
    rollno3 = fields.Char('Registration number')
    sc_From1 = fields.Date('Batch From')
    sc_To1 = fields.Date('Batch To')
    sc_From2 = fields.Date('Batch From')
    sc_To2 = fields.Date('Batch To')
    sc_From3 = fields.Date('Batch From')
    sc_To3 = fields.Date('Batch To')






    job_position = fields.Char('Applying Position')
    joining_date = fields.Date('joining date')
    office_address = fields.Char('office address')
    office_name = fields.Char('Company name')
    job_salary = fields.Char('salary for position')
    reporting_manager = fields.Char('Reporting Manager')
    mngr_position = fields.Char('Manager position')


 
    

 
    
    Achievement = fields.Text(string="Any Achievements")
    dg_percentage = fields.Integer('Percentage Or CGPA')
    school = fields.Text(string="School Name ")
    school2 = fields.Text(string="School Name")



    sc_percentage = fields.Integer('Percentage')
    sc_percentage2 = fields.Integer('Percentage')

    employment_line_ids = fields.One2many('previous.employment.lines','subline_id', string = 'Employment Details')


    
    email_id = fields.Char(string="Email")
    about = fields.Text(string="About")
    refernece_name = fields.Char(string="Reference name")
    refernece_position = fields.Char(string="Reference position")
    refernece_email = fields.Char(string="Reference email")
    refernece_mobile = fields.Char(string="Referenece mobile number")

    skills = fields.One2many('employe.resume','employee_skills_lines', string = 'Skills')

    language_speak = fields.One2many('arun.test','language_lines', string = 'Language')

    degree = fields.Selection([
    ('Associates degree','Associates degree'),
    ('Bachelors degree', 'Bachelors degree'),
    ('Masters degree', 'Masters degree'),
    ('Research doctorate', 'Research doctorate'),
    ('professional degree', 'professional degree'),
    ('Honorary doctorate', 'Honorary doctorate'),
    ], string="Degree",)

    department = fields.Selection([
    ('Chemical Engineering','Chemical Engineering'),
    ('Civil and Environmental Engineering', 'Civil and Environmental Engineering'),
    ('Computer Science Engineering', 'Computer Science Engineering'),
    ('Information Technology', 'Information Technology'),
    ('Industrial and Systems Engineering', 'Industrial and Systems Engineering'),
    ('Mechanical Engineering', 'Mechanical Engineering'),
    ('Art & Design', 'Art & Design'),
    ('Chemistry and Biochemistry', 'Chemistry and Biochemistry'),
    ('Accounting', 'Accounting'),
    ('Construction Management', 'Construction Management'),
    ('Economics and Finance', 'Economics and Finance'),
    ('Information Systems Analysis', 'Information Systems Analysis'),
    ('Management Information Systems', 'Management Information Systems'),
    ('M.B.A.', 'M.B.A.'),
    ('Sociology, Social Work and Criminal Justice', 'Sociology, Social Work and Criminal Justice'),
    ('Mathematics', 'Mathematics'),
    ('Political Science', 'Political Science'),
    ('University Studies', 'University Studies'),
    ('JoAnne Gay Dishman School of Nursing', 'JoAnne Gay Dishman School of Nursing'),
    ('General Business', 'General Business'),
    ('Deaf Studies and Deaf Education', 'Deaf Studies and Deaf Education'),
    ('Communication and Media', 'Communication and Media'),

    ], string="Department",)
    







    age_group = fields.Selection([
        ('major', 'Major'),
        ('minor', 'Minor'),
    ], string="Age Group", compute='set_age_group', store=True, readonly = 1)

    @api.constrains('dg_percentage')
    def set_degree_limit(self):
        for rec in self:
            if rec.dg_percentage:
                if rec.dg_percentage < 60:
                    raise ValidationError("Eligibility criteria for degree percentage is 60 and above")
                    


    @api.depends('test_age')
    def set_age_group(self):
        for rec in self:
            if rec.test_age:
                if rec.test_age < 18:
                    rec.age_group = 'minor'
                else:
                    rec.age_group = 'major'
    
    @api.onchange('test_age')
    def _onchange_start_date(self):
        i = 11
        while self.test_age < i :
            return {
                'warning': {

                    'title':"Not Eligible",
                    'message' :"Sorry for Incovinience!\n"
                                 "Candiates of age below bar category is not eligible"

                }
            }
    @api.onchange('test_age')
    def _onchange_birth_date(self):
        i = 50
        while self.test_age >i & i :
            return {
                'warning': {

                    'title':"Not Eligible",
                    'message' :"Sorry for Incovinience!\n"
                                "Candiates of age  50 and above category is not eligible"

                }
            }

    
    
class sample_line_subline(models.Model):
    _name = "previous.employment.lines"
    _description = 'Previous employment details'


    empployment_name = fields.Char(string="Company name")
    employment_id = fields.Char('Emp ID')
    empployment_title = fields.Char(string="Job Title")
    from_date = fields.Date('From Date')
    To_date = fields.Date('To Date')
    employment_salary = fields.Integer('Salary/year')
    employment_resignation = fields.Char(string="Reason for leaving")
    empployment_address = fields.Char(string="Emp Company address")


    subline_id = fields.Many2one('arun.test', string = 'Employment')


class resume_format(models.Model):
    _name = "employe.resume"
    _description = 'Resume build format'


    # employee_skills1 = fields.Char(string="Skill sets")
    # employee_skills =fields.Selection([
    #     ('male', 'Male'),
    #     ('female', 'Female'),
    # ], default='male', string="Gender")
    employee_skills = fields.Selection([
    ('','select'),
    ('odoo', 'ODOO'),
    ('python', 'Python programming Language'),
    ('java', 'Java programming Language'),
    ('c', 'C programming Language'),
    ('c++', 'C ++ programming Language'),
    ('oops', 'Objects Orieneted programming Language'),
    ('machine learning', 'Machine Learning'),
    ('c#', 'c#'),
    ('html', 'HTML and CSS'),
    ('iot', 'Interenet of Things'),
    ('sap', 'SAP'),
    ('odooerp', 'ODOO ERP'),
    ('sales', 'Sales Management'),
    ('data', 'Data Analysis'),
    ('team', 'Team Leadership'),
    ('communication', 'Good Communication'),
    ('order', 'Order To Cash'),
    ('pogramming', 'Programming'),
    ('linux', 'Linux'),
    ('arudino', 'Arduino'),
    ('electical', 'Electrical and Electronics'),
    ('industry', 'Industry'),
    ('chemical', 'Chemical'),
    ('networking', 'Networking'),
    ], default='select skills', string="Skill sets" ,)

    employee_skills_lines = fields.Many2one('arun.test', string = 'Employee_resume')




class ResPartner(models.Model):
    _inherit = "res.partner"
    _inherit = "arun.test"

    street = fields.Char(string= "address")
    street2 = fields.Char()
    city = fields.Char()
    country_id = fields.Many2one('res.country', 'Country')
    state_id = fields.Many2one('res.country.state', 'state')
    zip = fields.Char(string="ZIP")


    current_street = fields.Char(string= "address")
    current_street2 = fields.Char()
    current_city = fields.Char()
    current_country_id = fields.Many2one('res.country', 'Country')
    current_state_id = fields.Many2one('res.country.state', 'state')
    current_zip = fields.Char(string="ZIP")

    type = fields.Selection(string='Type',selection=[('Toggle if Both permanet and current address is same', 'Toggle if Both permanet and current address is same'), ('Toggle if Both permanet and current address is different', 'Toggle if Both permanet and current address is different')])

    
    language = fields.Selection([
    ('select','select'),
    ('english', 'English'),
    ('hindi', 'HINDI'),
    ('tamil', 'TAMIL'),
    ('french', 'FRENCH'),
    ('russian', 'RUSSIAN'),
    ('bengali', 'BENGALI'),
    ('telugu', 'TELUGU'),
    ('spanish', 'SPANISH'),
    ('portuguese', 'PORTUGUESE'),
    ('chinese', 'CHINESE'),
    ('japanese', 'JAPANESE'),
    ('arabic', 'ARABIC'),
    ('urudu', 'URUDU'),
    ('punjabhi', 'PUNJABHI'),
    ('korean', 'KOREAN'),
    ('turkish', 'TURKISH'),
    ('german', 'GERMAN'),
    ], 'language', default="select")
    language_lines = fields.Many2one('arun.test', string = 'Employee_language')

    maritial_status = fields.Selection([
    ('select','select'),
    ('married', 'MARRIED'),
    ('single', 'SINGLE'),
    ], default="select",string="MARITIAL STATUS" ,)

    aadhar_no = fields.Char(string="Aadhar card No:")
    pan_no = fields.Char(string="PAN NO:")

    selected_position = fields.Char(string="Selected Position")
    expected_salary =fields.Integer('Expected Salary')
    previous_salary = fields.Integer('Previous Salary')
    availability_date = fields.Date('Availability Date')
    notice_period = fields.Integer('Notice Period in Days')
