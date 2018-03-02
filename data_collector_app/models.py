from django.db import models

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
prisoners_wivies = 'Prisoners wivies' # form says 'Prisoners Widows' Confirm this
govt_workers = 'Government workers (work place)'
sex_workers = 'Sex workers'
church_leaders = 'Church leaders'
employee_families = 'Employees and/or Employee families'
gdwg = 'Guardians/ Divorced/ Widows/ Grandparents'
idu = 'Intravenous drug users (IDU)'
msm = 'Men who have sex with men (MSM)'
mobile_population = 'Migrants/ Mobile population'
out_of_school_youth = 'Out of school youth'
prisoners = 'Prisoners'
street_children = 'Street children'
traditional_healers = 'Traditional healers'
traditional_leaders = 'Traditional leaders'
target_others = 'Other target groups - please specify' # change some kind of list later

grants = 'Grants'
technical_support = 'Technical support'
infrastructure = 'Infrastructure'
training = 'Training'
materials = 'Materials'
area_others = 'Other areas (please specify)'

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
other = 'Other' # Enter from keyboard -- customized field 

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
    (prisoners_wivies, 'Prisoners wivies'),
    (govt_workers, 'Government workers (work place)'),
    (sex_workers, 'Sex workers'),
    (church_leaders, 'Church leaders'),
    (employee_families, 'Employees and/or Employee families'),
    (gdwg, 'Guardians/ Divorced/ Widows/ Grandparents'),
    (idu, 'Intravenous drug users (IDU)'),
    (msm, 'Men who have sex with men (MSM)'),
    (mobile_population, 'Migrants/ Mobile population'),
    (out_of_school_youth, 'Out of school youth'),
    (prisoners, 'Prisoners'),
    (street_children, 'Street children'),
    (traditional_healers, 'Traditional healers'),
    (traditional_leaders, 'Traditional leaders'),
    (target_others, 'Other target groups - please specify')
)

DISTRICT_AREA_LIST = () # Auto populated area tuple from, dependant on district 

TYPE_OF_SUPPORT_LIST = (
    (grants, 'Grants'),
    (technical_support, 'Technical support'),
    (infrastructure, 'Infrastructure'),
    (training, 'Training'),
    (materials, 'Materials'),
    (area_others, 'Other areas (please specify)')
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
    (other, 'Other')
)

#               STAKEHOLDER DIRECTORY
# *************************************************

class BasicDetails(models.Model):
    # --> Basic details on the organization
    organization_name = models.CharField(max_length=200)
    start_year = models.DateTimeField('start_year')
    permanent_employee_female = models.IntegerField(default=0)
    permanent_employee_male = models.IntegerField(default=0)
    temporary_employee_female = models.IntegerField(default=0)
    temporary_employee_male = models.IntegerField(default=0)
    volunteer_employee_female = models.IntegerField(default=0)
    volunteer_employee_male = models.IntegerField(default=0)
    description = models.TextField()

class ContactDetails(models.Model):
    # --> Contact details
    contact_name = models.CharField(max_length=50)
    contact_organization = models.CharField(max_length=100)
    contact_address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    alternative_phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    organization_type = models.CharField(max_length=100, choices=ORGANIZATION_TYPE_LIST, default='N/A')
    organization_target = models.CharField(max_length=100, choices=ORGANIZATION_TARGET_LIST, default='N/A')

class GeographicActivities(models.Model):
    # --> Geographic activities - High impact interventions
    elimination_of_mother_child_transmission = models.BooleanField()
    condom_programming = models.BooleanField()
    voluntary_medical_male_circumcision = models.BooleanField()
    hiv_counselling_testing = models.BooleanField()
    social_behaviour_change = models.BooleanField()
    anti_retroviral_treatment = models.BooleanField()

    # --> Geographic activities - Critical enablers
    gender_equality_empowerment = models.BooleanField()
    laws_legal_policies_practices = models.BooleanField()
    leadership_commitment_good_governance = models.BooleanField()
    resource_mobilization_sustainable_financing = models.BooleanField()

    # --> Geographic activities - Synergies with development sectors
    post_exposure_prophylaxis = models.BooleanField()
    blood_safety = models.BooleanField()
    poverty_alleviation_livelihoods = models.BooleanField()
    food_nutrition_security = models.BooleanField()
    mainstreaming_hiv_into_capital_projects = models.BooleanField()

class FundingSources(models.Model):
    # --> Funding sources
    funder_organization = models.CharField(max_length=100)
    funder_support_type = models.CharField(max_length=100, choices=ORGANIZATION_TYPE_LIST, default='N/A')
    amount = models.IntegerField()
    comment = models.TextField()

class TargetGroupMessages(models.Model):
    # --> Target groups and prevention messages
    condom_use = models.CharField(max_length=100, choices=ORGANIZATION_TARGET_LIST, default='N/A')
    mc_information = models.CharField(max_length=100, choices=ORGANIZATION_TARGET_LIST, default='N/A')
    mcp_information = models.CharField(max_length=100, choices=ORGANIZATION_TARGET_LIST, default='N/A')
    pmtct_promotion = models.CharField(max_length=100, choices=ORGANIZATION_TARGET_LIST, default='N/A')
    vct_hct_promotion = models.CharField(max_length=100, choices=ORGANIZATION_TARGET_LIST, default='N/A')
    pep_information = models.CharField(max_length=100, choices=ORGANIZATION_TARGET_LIST, default='N/A')
    sti_information = models.CharField(max_length=100, choices=ORGANIZATION_TARGET_LIST, default='N/A')
    tb_information = models.CharField(max_length=100, choices=ORGANIZATION_TARGET_LIST, default='N/A')
    gbv_information = models.CharField(max_length=100, choices=ORGANIZATION_TARGET_LIST, default='N/A')
    social_norms = models.CharField(max_length=100, choices=ORGANIZATION_TARGET_LIST, default='N/A')
    message_other = models.CharField(max_length=100, choices=ORGANIZATION_TARGET_LIST, default='N/A')


# HIV ACTIVITIES ORGANIZATION PARTICIPATES IN FORM
# *************************************************

'''
# --> Social behaviour change communication
class Actives(models.Model):

    IEC_produced_num = models.CharField(max_length=50, choices=IEC_MATERIALS)
    IEC_distributed_num = models.CharField(max_length=50, choices=IEC_MATERIALS)

    in_school
    in_school_female_num
    in_school_male_num

teachers
teachers_female_num
teachers_male_num

out_school
out_school_female_num
out_school_male_num

sex_workers
sex_workers_female_num
sex_workers_male_num

prisoners
prisoners_female_num
prisoners_male_num

pwd
pwd_female_num
pwd_male_num

ltd
ltd_female_num
ltd_male_num

# --> Condom programming
outlets_supplied
condom_distributed
condom_distributed_female_num
condom_distributed_male_num

# --> Critical enablers
total_victim_per_quarter

victim_less_fifteen
victim_less_fifteen_female_num
victim_less_fifteen_male_num

victim_more_fifteen
victim_more_fifteen_female_num
victim_more_fifteen_male_num

accessed_pep
accessed_pep_female_num
accessed_pep_male_num

funding_spent

# --> Synergies with other development sectors
action_plan

work_programmes

employees_reached
employees_reached_female_num
employees_reached_male_num

capital_projects

# --> Community health systems
plhiv_groups

plhiv_female_num
plhiv_male_num

ovc_female_num
ovc_male_num

# --> Monitoring and Evaluation
functional_systems
designated_systems

'''