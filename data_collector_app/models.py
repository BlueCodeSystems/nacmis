from django.db import models

# Create your models here.

list_type_of_organization = ['CBO', 'FBO', 'Local NGO', 'International NGO', 'Government', 'Private']

#               STAKEHOLDER DIRECTORY
# *************************************************

# --> Basic details on the organization
organization_name
start_year
permanent_employee_female
permanent_employee_male
temporary_employee_female
temporary_employee_male
volunteer_employee_female
volunteer_employee_male
description

# --> Contact details
contact_name
contact_organization
contact_address
phone
alternative_phone
email
website
organization_type
organization_target

# --> Geographic activities - High impact interventions
elimination_of_mother_child_transmission
condom_programming
voluntary_medical_male_circumcision
hiv_counselling_testing
social_behaviour_change
anti_retroviral_treatment

# --> Geographic activities - Critical enablers
gender_equality_empowerment
laws_legal_policies_practices
leadership_commitment_good_governance
resource_mobilization_sustainable_financing

# --> Geographic activities - Synergies with development sectors
post_exposure_prophylaxis
blood_safety
poverty_alleviation_livelihoods
food_nutrition_security
mainstreaming_hiv_into_capital_projects

# --> Funding sources
funder_organization
funder_support_type
amount
comment

# --> Target groups and prevention messages
target_groups_care_givers
target_groups_children
target_groups_church_leaders
target_groups_sex_workers
target_groups_disabled_persons
target_groups_employee_families
target_groups_government_workers
target_groups_gdwg
target_groups_heath_workers
target_groups_Idu
target_groups_msm
target_groups_mobile_population
target_groups_old_people
target_groups_ovc
target_groups_out_of_school_youth
target_groups_plhiv
target_groups_pregnant_women
target_groups_prisoners
target_groups_street_children
target_groups_teachers
target_groups_traditional_healers
target_groups_traditional_leaders
target_groups_truck_drivers
target_groups_youth
target_groups_others
'''

#               REPORT DETAIL FORM
# *************************************************
class ReportDetail(models.Model):
    # list variables
    cbo = 'Community Based Organization'
    fbo = 'Faith Based Organization'
    local_ngo = 'Local NGO'
    inter_ngo = 'International NGO'
    government = 'Government Organization'
    private = 'Private Organization'

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
        (private, 'Private Organization')
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

    # DISTRICT to load from another system

    report_date = models.DateTimeField('date of report')
    quarter = models.CharField(max_length=50, choices=QUARTER_LIST)
    name = models.CharField(max_length=200)
    organization_type = models.CharField(max_length=100, choices=ORGANIZATION_TYPE_LIST, default='N/A')
    location = models.CharField(max_length=100)
    reporter_name = models.CharField(max_length=100, help_text='Full names of person compiling the report.')
    reporter_phone = models.CharField(max_length=50, help_text='Number of person compiling the report. Enter digits only.')
    reporter_email = models.CharField(max_length=100, help_text='format example@company.com')

# HIV ACTIVITIES ORGANIZATION PARTICIPATES IN FORM
# *************************************************

# --> Social behaviour change communication
class Actives(models.Model):
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

    IEC_MATERIALS = (
        (books, 'Books'),
        (brochures, 'Brochures'),
        (posters = 'Posters'),
        (t_shirts, 'T-Shirts'),
        (tv_spots, 'TV Spots'),
        (radio_spots, 'Radio Spots'),
        (e_spots, 'E spot'),
        (billboards, 'Billboards'),
        (drama, 'Drama'),
        (other, 'Other')
    )

    IEC_produced_num = models.CharField(max_length=50, choices=IEC_MATERIALS)
    IEC_distributed_num = models.CharField(max_length=50, choices=IEC_MATERIALS)

    in_school
    in_school_female_num
    in_school_male_num
'''
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