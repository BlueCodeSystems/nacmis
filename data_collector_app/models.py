from django.db import models
from django import forms

# Create your models here.
# list variables
cbo = 'Community Based Organization'
fbo = 'Faith Based Organization'
local_ngo = 'Local NGO'
inter_ngo = 'International NGO'
government = 'Government Organization'
private = 'Private Organization'
org_others = 'Other organization / group - please specify'  # change some kind of list later

lsk = 'Lusaka Province'
cop = 'Copperbelt Province'
east = 'Easten Province'
lua = 'Luapula Province'
much = 'Muchinga Province'
nwest = 'North Westen Province'
north = 'Northern Province'
south = 'Southern Province'
west = 'Western Province'

Q1 = 'Quarter 1'
Q2 = 'Quarter 2'
Q3 = 'Quarter 3'
Q4 = 'Quarter 4'

plhiv = 'People living with HIV/ AIDS (PLHIV)'
ovc = 'Orphans and Vulnerable Children (OVC)'
pregnant_women = 'Pregnant Women'
care_givers = 'Care givers'
health_workers = 'Heath workers'
teachers = 'Teachers'
children = 'Children'
adolecents = 'Adolecents/ Youth'
old_people = 'Old people/ Pensioners'
disabled_people = 'Disabled people'
inmates_wivies = 'Prisoners wivies' # form says 'Prisoners Widows' Confirm this
govt_workers = 'Government workers (work place)'
sex_workers = 'Sex workers'
church_leaders = 'Church leaders'
employee_families = 'Employees and/or Employee families'
gdwg = 'Guardians/ Divorced/ Widows/ Grandparents'
idu = 'Intravenous drug users (IDU)'
msm = 'Men who have sex with men (MSM)'
mobile_population = 'Migrants/ Mobile population'
out_of_school_youth = 'Out of school youth'
inmates = 'Inmates'
street_children = 'Street children'
traditional_healers = 'Traditional healers'
traditional_leaders = 'Traditional leaders'
target_others = 'Other target groups - please specify' # change some kind of list later

food_and_nutrition = 'Food and Nutrition'
shelter_and_care = 'Shelter and Care'
protection_and_legal_aid = 'Protection and Legal aid'
healthcare = 'Healthcare'
psychosocial = 'Psychosocial'
social_support = 'Social support'
spiritual_support = 'Spiritual support'
education_and_vocational_training = 'Education and Vocational training'
economic_strengthening = 'Economic strengthening'

n_a = 'N/A'
no = 'NO materials were distributed this quater'
books = 'Books'
brochures = 'Brochures'
posters = 'Posters'
t_shirts = 'T-Shirts'
tv_spots = 'TV Spots'
radio_spots = 'Radio Spots'
e_spots = 'E spot'
billboards = 'Billboards'
drama = 'Drama' # customized field
material_other = 'Other' # Enter from keyboard -- customized field 

nacmis = 'NAC-MIS'
hmis = 'HMIS'
datim = 'DATIM'
internal_system = 'Internal system'
systems_other = 'Other'

QUARTER_LIST = (
    (Q1, 'Jan - Mar'),
    (Q2, 'Apr - Jun'),
    (Q3, 'Jul - Oct'),
    (Q4, 'Nov - Dec')
)

ORGANIZATION_TYPE_LIST = (
    (cbo, 'Community Based Organization'),
    (fbo, 'Faith Based Organization'),
    (local_ngo, 'Local Non Governmental Organization'),
    (inter_ngo, 'International Non Governmental Organization'),
    (government, 'Government Organization'),
    (private, 'Private Organization'),
    (org_others, 'Other organization / group - please specify')
)

PROVINCES_ZAMBIA = (
    (lsk, 'Lusaka Province'),
    (cop, 'Copperbelt Province'),
    (east, 'Easten Province'),
    (lua, 'Luapula Province'),
    (much, 'Muchinga Province'),
    (nwest, 'North Westen Province'),
    (north, 'Northern Province'),
    (south, 'Southern Province'),
    (west, 'Western Province')
)

ORGANIZATION_TARGET_LIST = (
    (plhiv, 'People living with HIV/ AIDS'),
    (ovc, 'Orphans and Vulnerable Children'),
    (pregnant_women, 'Pregnant Women'),
    (care_givers, 'Care givers'),
    (health_workers, 'Heath workers'),
    (teachers, 'Teachers'),
    (children, 'Children'),
    (adolecents, 'Adolecents/ Youth'),
    (old_people, 'Old people/ Pensioners'),
    (disabled_people, 'Disabled people'),
    (inmates_wivies, 'Prisoners wivies'),
    (govt_workers, 'Government workers (work place)'),
    (sex_workers, 'Sex workers'),
    (church_leaders, 'Church leaders'),
    (employee_families, 'Employees and/or Employee families'),
    (gdwg, 'Guardians/ Divorced/ Widows/ Grandparents'),
    (idu, 'Intravenous drug users (IDU)'),
    (msm, 'Men who have sex with men (MSM)'),
    (mobile_population, 'Migrants/ Mobile population'),
    (out_of_school_youth, 'Out of school youth'),
    (inmates, 'Inmates'),
    (street_children, 'Street children'),
    (traditional_healers, 'Traditional healers'),
    (traditional_leaders, 'Traditional leaders'),
    (target_others, 'Other target groups - please specify')
)


DISTRICT_AREA_LIST = () # Auto populated area tuple from, dependant on district 

TYPE_OF_SUPPORT_LIST = (
    (food_and_nutrition, 'Food and Nutrition'),
    (shelter_and_care, 'Shelter and Care'),
    (protection_and_legal_aid, 'Protection and Legal aid'),
    (healthcare, 'Healthcare'),
    (psychosocial, 'Psychosocial'),
    (social_support, 'Social support'),
    (spiritual_support, 'Spiritual support'),
    (education_and_vocational_training, 'Education and Vocational training'),
    (economic_strengthening, 'Economic strengthening')
)

PREVENTION_MESSAGES_LIST = (
    ('Condom use','Condom use'),
    ('MC information','MC information'),
    ('MCP information','MCP information'),
    ('PMTCT Promotion','PMTCT Promotion'),
    ('VCT/ HCT Promotion','PMTCT Promotion')
)

IEC_MATERIALS = (
    (books, 'Books'),
    (brochures, 'Brochures'),
    (posters, 'Posters'),
    (t_shirts, 'T-Shirts'),
    (tv_spots, 'TV Spots'),
    (radio_spots, 'Radio Spots'),
    (e_spots, 'E spot'),
    (billboards, 'Billboards'),
    (drama, 'Drama'),
    (material_other, 'Other')
)

SOURCES_OF_INFORMATION = (
    (nacmis, 'NAC-MIS'),
    (hmis, 'HMIS'),
    (datim, 'DATIM'),
    (internal_system, 'Internal system'),
    (systems_other, 'Other')
)
AREA_OF_SUPPORT = (
    ("High impact interventions", (
        ('condom_programming', 'Condom Programming'),
        ('hiv_conselling_and_testing', 'HIV Conselling and Testing'),
    )
    ),
    ("Critical enablers", (
        ('gender_equality_and_empowerment', 'Gender equality and Empowerment'),
        ('leadership_commitment_and_good_governance', 'Leadership Commitment and Good Governance'),
    )
    )
)

PROVINCE_DISTRICTS = (
    ("Muchinga", (
        ('Chama', 'Chama'),
        ('Chinsali', 'Chinsali'),
        ('Isoka', 'Isoka')
    )
    ),
    ("Lusaka", (
        ('Lusaka', 'Lusaka'),
        ('Chilanga', 'Chilanga'),
        ('Kafue', 'Kafue')
    )
    )
)


#               HELPER CLASSES FOR STAKEHOLDER DIRECTORY
# *********************************************************************
class OrganizationType(models.Model):
    organization_type_option = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.organization_type_option

class OrganizationTarget(models.Model):
    # Which group(s) does your organization target? (Please tick as many different groups that 
    # are targeted by your organization)
    organization_target_option = models.CharField(max_length=100, choices=ORGANIZATION_TARGET_LIST, default="")   # removed choice for more flexibility

    def __str__(self):
        return self.organization_target_option

#                   STAKEHOLDER DIRECTORY
# ************************************************************

class StakeHolder(models.Model):
    # --> Basic details on the organization
    organization_name = models.CharField(max_length=200)
    start_year = models.DateField('which year did your organization start working in this district?')
    permanent_employee_female = models.IntegerField('current number of permanent female employees', default=0)
    permanent_employee_male = models.IntegerField('current number of permanent male employees', default=0)
    temporary_employee_female = models.IntegerField('current number of temporary female employees', default=0)
    temporary_employee_male = models.IntegerField('current number of temporary male employees', default=0)
    volunteer_employee_female = models.IntegerField('current number of volunteer female employees', default=0)
    volunteer_employee_male = models.IntegerField('current number of volunteer male employees', default=0)
    description_of_organization = models.TextField('Brief description of the organization (Please describe your \
        organization in no more than 50 words)')

    # --> Contact details
    key_contact_name = models.CharField('name of key contact person', max_length=50)
    position_within_organization = models.CharField(max_length=50)
    organization_district = models.CharField(max_length=200, choices=PROVINCE_DISTRICTS)
    organization_address = models.CharField('street address of the organization', max_length=100)
    telephone_number = models.CharField('telephone number', max_length=20)
    telephone_number_alternative = models.CharField('Telephone number alternative', max_length=20)
    email_address = models.EmailField('email address', max_length=254)
    website = models.URLField(max_length=200)

    organization_type = models.CharField(max_length=100, choices=ORGANIZATION_TYPE_LIST)
    
    organization_target = models.ManyToManyField(OrganizationTarget)

    def __str__(self):
        return self.organization_name + ' - ' + self.organization_district + ' - ' + self.telephone_number

    # --> Geographic activities - High impact interventions
    # What area(s) of support does your organization provide? (Please tick as many different areas that 
    # are carried out by your organization)

    # --> Funding sources
    # Please provide details on the organization that provide funding to you, starting with the largest 
    # partner/ donor. We also want to understand the types of support that the partners/donors provide to 
    # your organization, and the funding each partner/ donor has given you 2016. (The information on funding 
    # will not be published and only held at DAFT) 

    # --> Target groups and prevention messages
    # Using the matrix below please hoghlight with a tick where your organization is/ will be providing 
    # prevention messages to one or more of the target groups listed

class GeographicActivity(models.Model):
    area_of_support = models.CharField(max_length=100, choices=AREA_OF_SUPPORT, default="")
    location = models.CharField(max_length=100, choices=PROVINCE_DISTRICTS, default="")
    organization = models.ForeignKey(StakeHolder, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.area_of_support + '-' + self.location

class TargetGroupPreventionMessages(models.Model):
    target_group = models.CharField(max_length=100, choices=ORGANIZATION_TARGET_LIST, default="")
    prevention_message = models.CharField(max_length=100, choices=PREVENTION_MESSAGES_LIST, default="")
    organization = models.ForeignKey(StakeHolder, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.target_group + " " + self.prevention_message

class FundingSources(models.Model):
    name_of_organization =  models.CharField(max_length=100, default="")
    funding_amount =  models.IntegerField()
    organization = models.ForeignKey(StakeHolder, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_of_organization


class TypesOfFundingSupport(models.Model):
    support_option =  models.CharField(max_length=100, default="")
    funding_source = models.ForeignKey(FundingSources, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.support_option


# HIV ACTIVITIES ORGANIZATION PARTICIPATES IN FORM
# *************************************************
    
class ActivityReportForm(models.Model):
    # Stake holder directory to SARF ---> one-to-many relationship
    stake_holder = models.ForeignKey(StakeHolder, on_delete=models.SET_NULL, null=True)
    report_date = models.DateField(null=True)
    #types_of_support = models.CharField(max_length=200, choices=TYPES_OF_SUPPORT_LIST)
    quarter_been_reported_on = models.CharField(max_length=20, choices=QUARTER_LIST)
    name = models.CharField(max_length=50)
    telephone_number = models.CharField(max_length=20)
    email_address = models.EmailField(max_length=50)


    # Types of care and support organization provides
    food_and_nutrition = models.BooleanField()
    shelter_and_care = models.BooleanField()
    protection_and_legal_aid = models.BooleanField()
    healthcare = models.BooleanField()
    psychosocial = models.BooleanField()
    social_support = models.BooleanField()
    spiritual_support = models.BooleanField()
    education_and_vocational_training = models.BooleanField()
    economic_strengthening = models.BooleanField()

    # Monitoring and Evaluation
    nacmis = models.BooleanField('NAC-MIS')
    hmis = models.BooleanField('HMIS')
    datim = models.BooleanField('DATIM')
    internal_system = models.BooleanField('Internal system')
    systems_other = models.BooleanField('Other')

class IECMaterial(models.Model):
    # --> Social behaviour change communication
    material_type = models.CharField(max_length=100, choices=IEC_MATERIALS, default='N/A')
    number_distributed = models.IntegerField('number of materials distributed', default=0)
    localized = models.BooleanField(default=False)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

# --> Social behaviour change communication for key populations
  
class AdolecentsReached(models.Model):
    # in_school
    # Number of adolescents and young people aged 10-24 reached by IEC materials by your 
    # organization this quarter
    adolescents_female_10_14 = models.IntegerField('female adolescents of ages 10 to 14', default=0)
    adolescents_female_15_19 = models.IntegerField('female adolescents of ages 15 to 19', default=0)
    adolescents_female_20_24 = models.IntegerField('female adolescents of ages 20 to 24', default=0)

    adolescents_male_10_14 = models.IntegerField('male adolescents of ages 10 to 14', default=0)
    adolescents_male_15_19 = models.IntegerField('male adolescents of ages 15 to 19', default=0)
    adolescents_male_20_24 = models.IntegerField('male adolescents of ages 20 to 24', default=0)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class OutOfSchool(models.Model):
    # out_school
    # Number of Out of School children and young people aged 10-24 years provided with life
    # skills- based comprehensive sexuality education within this quarter
    out_school_female_10_14 = models.IntegerField('out of school females of ages 10 to 14', default=0)
    out_school_female_15_19 = models.IntegerField('out of school females of ages 15 to 19', default=0)
    out_school_female_20_24 = models.IntegerField('out of school females of ages 20 to 24', default=0)

    out_school_male_10_14 = models.IntegerField('out of school males of ages 10 to 14', default=0)
    out_school_male_15_19 = models.IntegerField('out of school males of ages 15 to 19', default=0)
    out_school_male_20_24 = models.IntegerField('out of school males of ages 20 to 24', default=0)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class SexWorker(models.Model):
    # sex_workers
    # How many sex workers were reached with HIV prevention programmes by your organization this quarter?
    sex_workers_female_num = models.IntegerField('female sex workers reached', default=0)
    sex_workers_male_num = models.IntegerField('male sex workers reached', default=0)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class Inmate(models.Model):
    # inmates
    # How many inmates were reached with HIV prevention programmes by your organization this quarter?
    inmates_female_num = models.IntegerField('female inmates reached', default=0)
    inmates_male_num = models.IntegerField('male inmates reached', default=0)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class CorrectionalFaciltyStaff(models.Model):
    # correctional facility staff
    # How many correctional facility staff were reached with HIV prevention programmes this quarter?
    correctional_staff_female_num = models.IntegerField('female correctional facility staff reached', default=0)
    correctional_staff_male_num = models.IntegerField('male correctional facility staff reached', default=0)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class PersonsWithDisabilty(models.Model):
    # persons with disabilty
    # How many persons with disability were reached with HIV prevention programmes by your organization this quarter?"
    pwd_female_num = models.IntegerField('female persons with disabilities reached', default=0)
    pwd_male_num = models.IntegerField('male persons with disabilities reached', default=0)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class MobileWorker(models.Model):
    # mobile workers
    # How many mobile workers were reached with HIV prevention programmes by your organization this quarter?
    mobile_workers_female_num = models.IntegerField('female mobile workers reached', default=0)
    mobile_workers_male_num = models.IntegerField('male mobile workers reached', default=0)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class MenWithMen(models.Model):
    # men who have sex with men
    # How many men who have sex with men (MSM) were reached with HIV prevention programmes by your 
    # organization this quarter?
    men_with_men = models.IntegerField('men who have sex with men (MSM) reached', default=0)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class CondomProgramming(models.Model):
    # Condom programming
    # 1. How many condom service distribution points were supplied by your organization this 
    # quarter? (*excluding health facilities)
    # 2. How many male and/or female condoms were distributed to end users by your organization 
    # this quarter (excluding health facilities)?
    condom_dist_point_num = models.IntegerField('number of distribution points', default=0)
    female_condom_distributed_num = models.IntegerField('female condoms distributed', default=0)
    male_condom_distributed_num = models.IntegerField('male condoms distributed', default=0)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class CriticalEnabler(models.Model):
    
    # Crtical enablers
    #  Number of people who experienced physical or sexual violence and were referred for Post 
    # Exposure Prophylaxis (PEP) within 72 hours in accordance with national guidelines this quarter.
    accessed_pep_female_num = models.IntegerField('females who experienced physical or \
        sexual violence, and accessed Post Exposure Prophylaxis (PEP)', default=0)
    accessed_pep_male_num = models.IntegerField('males who experienced physical or sexual \
        violence, and accessed Post Exposure Prophylaxis (PEP)', default=0)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class SynergyDevelopmentSector(models.Model):
    # Synergies with other development sectors
    # How many employees were reached through workplace programmes by your organization this quarter?
    employees_reached_female_num = models.IntegerField('female employees reached through \
        workplace programmes', default=0)
    employees_reached_male_num = models.IntegerField('male employees reached through \
        workplace programmes', default=0)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class CommunityHealthSystem(models.Model):
    # Community health systems
    # 1. How many PLHIV support groups set up by your organization are currently active?
    # 2. How many PLHIV are currently enrolled in the active PLHIV support groups by your organization?
    plhiv_groups = models.IntegerField('PLHIV groups set up by your organization', default=0)
    plhiv_female_num = models.IntegerField('female persons living with HIV (PLHIV) currently \
        enrolled in active groups', default=0)
    plhiv_male_num = models.IntegerField('male persons living with HIV (PLHIV) currently \
        enrolled in active groups', default=0)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class VulnerablePeople(models.Model):
    # How many vulnerable people in total received care and support from your organization this quarter?
    ovc_female_num = models.IntegerField('female', default=0)
    ovc_male_num = models.IntegerField('male',default=0)
    ovc_care_support_0_9 = models.IntegerField('0 to 9', default=0)
    ovc_care_support_10_14 = models.IntegerField('10 to 14', default=0)
    ovc_care_support_15_19 = models.IntegerField('15 to 19', default=0)
    ovc_care_support_20_24 = models.IntegerField('20 to 24', default=0)
    ovc_care_support_25_plus = models.IntegerField('25 and above', default=0)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)
