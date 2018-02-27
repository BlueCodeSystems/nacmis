from django.db import models

# Create your models here.

#               REPORT DETAIL FORM
# *************************************************
class ReportDetail(models.Model):
    report_date = models.DateTimeField('date of report')
    quarter = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    report_type = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    reporter_name = models.CharField(max_length=100)
    reporter_phone = models.CharField(max_length=50)
    reporter_email = models.CharField(max_length=100)

# HIV ACTIVITIES ORGANIZATION PARTICIPATES IN FORM
# *************************************************

# --> Social behaviour change communication
IEC_produced_num
IEC_distributed_num

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


#               STAKEHOLDER DIRECTORY
# *************************************************

# --> Basic details on the organization
organization name
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
food_nutrition security
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