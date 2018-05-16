from phonenumber_field.modelfields import PhoneNumberField

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

lusaka = 'Lusaka Province'
central = 'Central Province'
copperbelt = 'Copperbelt Province'
eastern = 'Easten Province'
luapula = 'Luapula Province'
muchinga = 'Muchinga Province'
north_western = 'North Westen Province'
northern = 'Northern Province'
southern = 'Southern Province'
western = 'Western Province'

Q1 = 'Quarter 1'
Q2 = 'Quarter 2'
Q3 = 'Quarter 3'
Q4 = 'Quarter 4'

plhiv = 'People living with HIV/ AIDS (PLHIV)'
vp = 'Vulnerable People'
pregnant_women = 'Pregnant Women'
care_givers = 'Care givers'
health_workers = 'Heath workers'
teachers = 'Teachers'
adolecents = 'Adolecents/ Youth'
elderly = 'Elderly/ Pensioners'
persons_with_disabilities = 'Persons with Disabilities'
health_workers = 'Heath workers'
govt_workers = 'Government workers (work place)'
sex_workers = 'Sex workers'
widows = 'Widows'
pwid = 'People who Inject Drugs (PWID)'
msm = 'Men who have Sex with Men (MSM)'
inmates = 'Inmates'
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

yes = 'Yes'
no = 'No'

QUARTER_LIST = (
    (Q1, 'Jan - Mar'),
    (Q2, 'Apr - Jun'),
    (Q3, 'Jul - Oct'),
    (Q4, 'Nov - Dec')
)

ORGANIZATION_TYPE_LIST = (
    (cbo, 'Community Based Organization'),
    (fbo, 'Faith Based Organization'),
    (government, 'Government Organization'),
    (inter_ngo, 'International Non Governmental Organization'),
    (local_ngo, 'Local Non Governmental Organization'),
    (private, 'Private Organization'),
    (org_others, 'Other organization / group - please specify')
)

PROVINCES_ZAMBIA = (
    (lusaka, 'Lusaka Province'),
    (central, 'Central Province'),
    (copperbelt, 'Copperbelt Province'),
    (eastern, 'Easten Province'),
    (luapula, 'Luapula Province'),
    (muchinga, 'Muchinga Province'),
    (north_western, 'North Westen Province'),
    (northern, 'Northern Province'),
    (southern, 'Southern Province'),
    (western, 'Western Province')
)

PROVINCE_DISTRICTS = (
    (
        central, (
            ('Ben Kafupi', 'Ben Kafupi'),
            ('Justine Kabwe', 'Justine Kabwe'),
            ('Munyama', 'Munyama')
        )
    ),
    (
        copperbelt,(
            ('Ndola', 'Ndola'),
            ('Lufwanyama', 'Lufwanyama'),
            ('Mpongwe', 'Mpongwe')
        )
    ),
    (
        eastern,(
            ('Nyimba', 'Nyimba'),
            ('Vubwa', 'Vubwa'),
            ('Lundazi', 'Lundazi')
        )
    ),
    (
        luapula,(
            ('Samfya', 'Samfya'),
            ('Mansa', 'Mansa'),
            ('Mwansabombwe', 'Mwansabombwe')
        )
    ),
    (
        lusaka, (
            ('Lusaka', 'Lusaka'),
            ('Chilanga', 'Chilanga'),
            ('Kafue', 'Kafue')
        )
    ),
    (
        muchinga,(
            ('Mpika', 'Mpika'),
            ('Chinsali', 'Chinsali'),
            ('Mafinga', 'Mafinga')
        )
    ),
    (
        northern,(
            ('Mporokoso', 'Mporokoso'),
            ('Kasama', 'Kasama'),
            ('Mpulungu', 'Mpulungu')
        )
    ),
    (
        north_western,(
            ('Solwezi', 'Solwezi'),
            ('Mufumbwe', 'Mufumbwe'),
            ('Zambezi', 'Zambezi')
        )
    ),
    (
        southern,(
            ('Monze', 'Monze'),
            ('Kazungula', 'Kazungula'),
            ('Gwembe', 'Gwembe')
        )
    ),
    (
        western,(
            ('Mongu', 'Mongu'),
            ('Sikongo', 'Sikongo'),
            ('Sesheke', 'Sesheke')
        )
    )
)

# Auto populated ward area tuple from, dependant on district
DISTRICT_WARD_LIST = (
    (
        'Chilanga', (
            ('Nakachenje', 'Nakachenje'),
            ('Miteta', 'Miteta')
        )
    ),
    (
        'Gwembe', (
            ('Jumbo', 'Jumbo'),
            ('Siampande', 'Siampande')
        )
    ),
    (
        'Kabwe', (
            ('Highridge', 'Highridge'),
            ('Luansase', 'Luansase')
        )
    ),
    (
        'Kafue', (
            ('Chikupi', 'Chikupi'),
            ('Kasenje', 'Kasenje')
        )
    ),
    (
        'Kasama', (
            ('Julia Chikamoneka', 'Julia Chikamoneka'),
            ('Lualuo', 'Lualuo')
        )
    ),
    (
        'Kazungula', (
            ('Ngwezi', 'ward1'),
            ('Sikaunzwe', 'Sikaunzwe')
        )
    ),
    (
        'Lusaka', (
            ('Rapheal Chota', 'Rapheal Chota'),
            ('Roma', 'Roma')
        )
    ),
    (
        'Monze', (
            ('Mwanza West', 'Mwanza West'),
            ('Hatontola', 'Hatontola')
        )
    ),
    (
        'Mporokoso', (
            ('Chimpolonge', 'Chimpolonge'),
            ('Muchinga', 'Muchinga')
        )
    ),
    (
        'Mpulungu', (
            ('Isoko', 'Isoko'),
            ('Kapembwa', 'Kapembwa')
        )
    ),
    (
        'Solwezi', (
            ('Kapijimpanga', 'Kapijimpanga'),
            ('Tumvwanganai', 'Tumvwanganai')
        )
    )
)  

ORGANIZATION_TARGET_LIST = (
    (adolecents, 'Adolecents/ Youth'),
    (care_givers, 'Care givers'),
    (persons_with_disabilities, 'Persons with Disabilities'),
    (govt_workers, 'Government workers (work place)'),
    (health_workers, 'Heath workers'),
    (widows, 'Widows'),
    (inmates, 'Inmates'),
    (msm, 'Men who have sex with men (MSM)'),
    (elderly, 'Elderly/ Pensioners'),
    (vp, 'Vulnerable People'),
    (plhiv, 'People living with HIV/ AIDS'),
    (pregnant_women, 'Pregnant Women'),
    (sex_workers, 'Sex workers'),
    (teachers, 'Teachers'),
    (target_others, 'Other target groups - please specify')
)

TYPE_OF_SUPPORT_LIST = (
    (economic_strengthening, 'Economic strengthening'),
    (education_and_vocational_training, 'Education and Vocational training'),
    (food_and_nutrition, 'Food and Nutrition'),
    (healthcare, 'Healthcare'),
    (protection_and_legal_aid, 'Protection and Legal aid'),
    (psychosocial, 'Psychosocial'),
    (shelter_and_care, 'Shelter and Care'),
    (social_support, 'Social support'),
    (spiritual_support, 'Spiritual support')
)

PREVENTION_MESSAGES_LIST = (
    ('Condom use','Condom use'),
    ('MC information','MC information'),
    ('MCP information','MCP information'),
    ('PMTCT Promotion','PMTCT Promotion'),
    ('VCT/ HCT Promotion','VCT/ HCT Promotion')
)

IEC_MATERIALS = (
    (books, 'Books'),
    (billboards, 'Billboards'),
    (brochures, 'Brochures'),
    (drama, 'Drama'),
    (e_spots, 'E spot'),
    (posters, 'Posters'),
    (radio_spots, 'Radio Spots'),
    (tv_spots, 'TV Spots'),
    (t_shirts, 'T-Shirts'),
    (material_other, 'Other')
)

SOURCES_OF_INFORMATION = (
    (datim, 'DATIM'),
    (hmis, 'HMIS'),
    (internal_system, 'Internal system'),
    (nacmis, 'NAC-MIS'),
    (systems_other, 'Other')
)
AREA_OF_SUPPORT = (
    (
        "Critical enablers", (
            ('gender_equality_equity_and_empowerment', 'Gender Equality, Equity and Empowerment'),
            ('leadership_commitment_and_good_governance', 'Leadership Commitment and Good Governance'),
            ('policy_laws_and_human_rights', 'Policy, laws and human rights'),
            ('elimination_of_stigma_and_discrimination', 'Elimination of Stigma and Discrimination'),
            ('resource_mobilization_and_sustainable_financing', 'Resource Mobilization and Sustainable Financing'),
            ('positive_health_dignity_and_prevention', 'Positive Health Dignity and Prevention')
        )
    ),
    (
        "High impact interventions", (
            ('condom_programming', 'Condom Programming'),
            ('elimination_of_mother_to_child_transmission', 'Elimination of Mother to Child Transmission(eMTCT)'),
            ('voluntary_medical_male_circumcision', 'Voluntary Medical Male Circumcision(VMMC)'),
            ('hiv_testing_services', 'HIV Testing Services'),
            ('social_and_behaiviour_change_communication', 'Social and Behaiviour Change Communication'),
            ('hiv_tb_co_infection_treatment', 'HIV/TB Co-infection treatment'),
            ('provision_of_preexposure_prophylaxis', 'Provision of Pre-exposure Prophylaxis(PrEP)'),
            ('sti_screening_and_treatment', 'STI Screening and Treatment'),
            ('treatment_optimization', 'Treatment Optimization'),
            ('treatment_of_hiv_aids_sti_and_tb', 'Treatment of HIV/AIDS/STIs and TB')
        )
    ),
    (
        "Synergies with development sectors", (
            ('post_exposure_prophylaxis', 'Post Exposure Prophylaxis(PEP)'),
        )
    ),
    (
        "HIV and AIDS intergration and system strengthening", (
            ('integration_of_hiv_and_other_services', 
                'Integration of HIV/AIDS, Sexual reproduction Health and Other Services'),
        )
    ),
)

YES_OR_NO = (
    (yes, 'Yes'),
    (no, 'No')
)

#                       NATIONAL ORGANIZATION
# *********************************************************************
class NationalOrganization(models.Model):
    organization_name = models.CharField(max_length=200)
    organization_address = models.CharField('address of the organization', max_length=100)
    organization_contact_email = models.EmailField(max_length=254)

    def __str__(self):
        return self.organization_name + " - " + self.organization_contact_email

#               HELPER CLASSES FOR STAKEHOLDER DIRECTORY
# *********************************************************************
class District(models.Model):
    province = models.CharField(max_length=50, choices=PROVINCES_ZAMBIA, default="")
    name = models.CharField(max_length=50, choices=PROVINCE_DISTRICTS)

    def __str__(self):
        return self.name

class Ward(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class OrganizationType(models.Model):
    organization_type_option = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.organization_type_option

class OrganizationTarget(models.Model):
    # Which group(s) does your organization target? (Please tick as many different groups that 
    # are targeted by your organization)
    organization_target_option = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.organization_target_option

#                   STAKEHOLDER DIRECTORY
# ************************************************************

class StakeholderDirectory(models.Model):

    class Meta:
        verbose_name_plural = 'Stakeholder directories'

    # --> Basic details on the organization
    national_organization = models.ForeignKey(NationalOrganization, on_delete=models.CASCADE, null=True)
    organization = models.CharField(max_length=200)
    organization_address = models.CharField('address of the organization', max_length=100, blank=True)
    organization_district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    start_year = models.DateField('which year did your organization start working in this district?')
    gps = models.CharField('GPS Coordinates', max_length=20, blank=True)
    website = models.URLField(max_length=200, blank=True)
    description_of_organization = models.TextField('Brief description of the organization (Please describe your \
        organization in no more than 250 words)')

    # --> Contact details
    key_contact_name = models.CharField('name of key contact person', max_length=50)
    position_within_organization = models.CharField('position within the organization', max_length=50)
    telephone_number = PhoneNumberField()
    telephone_number_alternative = PhoneNumberField(blank=True)
    email_address = models.EmailField('email address', max_length=254)

    # --> Staff details
    permanent_employee_female = models.PositiveIntegerField('current number of permanent female employees', default=0)
    permanent_employee_male = models.PositiveIntegerField('current number of permanent male employees', default=0)
    temporary_employee_female = models.PositiveIntegerField('current number of temporary female employees', default=0)
    temporary_employee_male = models.PositiveIntegerField('current number of temporary male employees', default=0)
    volunteer_employee_female = models.PositiveIntegerField('current number of volunteer female employees', default=0)
    volunteer_employee_male = models.PositiveIntegerField('current number of volunteer male employees', default=0)

    # --> Organization Classification
    organization_type = models.CharField('which of the following \'types\' would best describe your \
        organization? (Please only tick one type of organization)', max_length=100, choices=ORGANIZATION_TYPE_LIST)
    organization_target = models.ManyToManyField(OrganizationTarget, verbose_name='which group(s) does your organization target? (please tick as many \
        different groups that are targeted by your organization)')

    def __str__(self):
        #return self.organization + ' - ' + self.organization_district + ' - ' + self.telephone_number
        return self.organization + ' - as stakeholder'

class SupportField(models.Model):
    area_of_support = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.area_of_support

class ProgramActivity(models.Model):
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, null=True)
    area_of_support = models.ManyToManyField(SupportField, verbose_name='Program activities by geographic area')
    organization = models.ForeignKey(StakeholderDirectory, on_delete=models.SET_NULL, null=True)

    #def __str__(self):
    #    return 'self.area_of_support.all() + '-' + self.ward.name

class FundingSource(models.Model):
    name_of_organization =  models.CharField(max_length=100, default="")
    funding_amount =  models.PositiveIntegerField('Funding Amount(In US Dollars)')
    organization = models.ForeignKey(StakeholderDirectory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_of_organization

class TargetGroupPreventionMessage(models.Model):
    prevention_message = models.CharField(max_length=100, choices=PREVENTION_MESSAGES_LIST, null=True)
    target_group = models.ManyToManyField(OrganizationTarget)
    organization = models.ForeignKey(StakeholderDirectory, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        #return self.target_group + " " + self.prevention_message
        return self.prevention_message

class TypesOfFundingSupport(models.Model):
    support_option =  models.CharField(max_length=100, default="")
    funding_source = models.ForeignKey(FundingSource, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.support_option

class OtherQuestion(models.Model):
    action_plan = models.CharField('Does you organization hava a current HIV and \
        AIDS action plan?', max_length=100, choices=YES_OR_NO);
    workplace_programme = models.CharField('Does your organization have a current \
        and active HIV and AIDS workplace programme?', max_length=20, choices=YES_OR_NO)
    sources_of_information = models.CharField('which sources of information does your \
        organization utilize to inform HIV programming and decision making?', max_length=20,
        choices=SOURCES_OF_INFORMATION)
    m_and_person = models.CharField('Does your organization have a designated M and E person?', 
        max_length=20, choices=YES_OR_NO)
    organization = models.ForeignKey(StakeholderDirectory, on_delete=models.CASCADE)

class EndOfYearQuestion(models.Model):
    funding = models.PositiveIntegerField('How much funding(in kwacha) was spent on HIV & \
        AIDS activities this year?')
    number_of_meetings_daft = models.PositiveIntegerField('How many DATIF meetings did your organization have \
        this year?')
    number_of_meetings_paft = models.PositiveIntegerField('How many PATIF meetings did your organization have \
        this year?')
    organization = models.ForeignKey(StakeholderDirectory, on_delete=models.CASCADE)

class GeneralComment(models.Model):
    general_comment = models.TextField(default="")
    organization = models.ForeignKey(StakeholderDirectory, on_delete=models.CASCADE)

# HIV ACTIVITIES ORGANIZATION PARTICIPATES IN FORM
# *************************************************
    
class ActivityReportForm(models.Model):
    report_date = models.DateField(null=True)
    quarter_been_reported = models.CharField(max_length=20, choices=QUARTER_LIST)
    stake_holder_name = models.ForeignKey(StakeholderDirectory, verbose_name='Name of the Organization', \
        on_delete=models.SET_NULL, null=True)
    
    # Location and Report Compilation section
    location_province = models.CharField('province', max_length=100, choices=PROVINCES_ZAMBIA, default="")
    location_district = models.CharField('district', max_length=100, choices=PROVINCE_DISTRICTS, default="")
    location_ward = models.CharField('ward', max_length=100, choices=DISTRICT_WARD_LIST, default="")
    name = models.CharField(max_length=50)
    telephone_number = PhoneNumberField()
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

    def __str__(self):
        if self.stake_holder_name:
            return self.stake_holder_name.organization + " - " + self.location_district + \
            " - " + self.quarter_been_reported
        else:
            return "unset stakeholder name"

# --> Social behaviour change communication 
class IECMaterial(models.Model):
    material_type = models.CharField(max_length=100, choices=IEC_MATERIALS, default='N/A')
    number_distributed = models.PositiveIntegerField('number of materials distributed', default=0)
    localized = models.BooleanField(default=False)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

    def __str__(self):
        return self.material_type

# --> Social behaviour change communication for key populations  
class AdolecentsReached(models.Model):
    adolescents_female_10_14 = models.PositiveIntegerField('female adolescents of ages 10 to 14', default=0)
    adolescents_female_15_19 = models.PositiveIntegerField('female adolescents of ages 15 to 19', default=0)
    adolescents_female_20_24 = models.PositiveIntegerField('female adolescents of ages 20 to 24', default=0)

    adolescents_male_10_14 = models.PositiveIntegerField('male adolescents of ages 10 to 14', default=0)
    adolescents_male_15_19 = models.PositiveIntegerField('male adolescents of ages 15 to 19', default=0)
    adolescents_male_20_24 = models.PositiveIntegerField('male adolescents of ages 20 to 24', default=0)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class OutOfSchool(models.Model):
    out_school_female_10_14 = models.PositiveIntegerField('out of school females of ages 10 to 14', default=0)
    out_school_female_15_19 = models.PositiveIntegerField('out of school females of ages 15 to 19', default=0)
    out_school_female_20_24 = models.PositiveIntegerField('out of school females of ages 20 to 24', default=0)

    out_school_male_10_14 = models.PositiveIntegerField('out of school males of ages 10 to 14', default=0)
    out_school_male_15_19 = models.PositiveIntegerField('out of school males of ages 15 to 19', default=0)
    out_school_male_20_24 = models.PositiveIntegerField('out of school males of ages 20 to 24', default=0)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class SexWorker(models.Model):
    sex_workers_female_num = models.PositiveIntegerField('female sex workers reached', default=0)
    sex_workers_male_num = models.PositiveIntegerField('male sex workers reached', default=0)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class Inmate(models.Model):
    inmates_female_num = models.PositiveIntegerField('female inmates reached', default=0)
    inmates_male_num = models.PositiveIntegerField('male inmates reached', default=0)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class CorrectionalFaciltyStaff(models.Model):
    correctional_staff_female_num = models.PositiveIntegerField('female correctional facility staff reached', default=0)
    correctional_staff_male_num = models.PositiveIntegerField('male correctional facility staff reached', default=0)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class PersonsWithDisabilty(models.Model):
    pwd_female_num = models.PositiveIntegerField('female persons with disabilities reached', default=0)
    pwd_male_num = models.PositiveIntegerField('male persons with disabilities reached', default=0)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class MobileWorker(models.Model):
    mobile_workers_female_num = models.PositiveIntegerField('female mobile workers reached', default=0)
    mobile_workers_male_num = models.PositiveIntegerField('male mobile workers reached', default=0)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class MenWithMen(models.Model):
    men_with_men = models.PositiveIntegerField('men who have sex with men (MSM) reached', default=0)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class CondomProgramming(models.Model):
    condom_dist_point_num = models.PositiveIntegerField('number of distribution points', default=0)
    female_condom_distributed_num = models.PositiveIntegerField('female condoms distributed', default=0)
    male_condom_distributed_num = models.PositiveIntegerField('male condoms distributed', default=0)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class CriticalEnabler(models.Model):
    accessed_pep_female_num = models.PositiveIntegerField('females who experienced physical or \
        sexual violence, and accessed Post Exposure Prophylaxis (PEP)', default=0)
    accessed_pep_male_num = models.PositiveIntegerField('males who experienced physical or sexual \
        violence, and accessed Post Exposure Prophylaxis (PEP)', default=0)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class SynergyDevelopmentSector(models.Model):
    employees_reached_female_num = models.PositiveIntegerField('female employees reached through \
        workplace programmes', default=0)
    employees_reached_male_num = models.PositiveIntegerField('male employees reached through \
        workplace programmes', default=0)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class CommunityHealthSystem(models.Model):
    plhiv_groups = models.PositiveIntegerField('PLHIV groups set up by your organization', default=0)
    plhiv_female_num = models.PositiveIntegerField('female persons living with HIV (PLHIV) currently \
        enrolled in active groups', default=0)
    plhiv_male_num = models.PositiveIntegerField('male persons living with HIV (PLHIV) currently \
        enrolled in active groups', default=0)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class VulnerablePeople(models.Model):
    ovc_female_num = models.PositiveIntegerField('female', default=0)
    ovc_male_num = models.PositiveIntegerField('male',default=0)
    ovc_care_support_0_9 = models.PositiveIntegerField('0 to 9', default=0)
    ovc_care_support_10_14 = models.PositiveIntegerField('10 to 14', default=0)
    ovc_care_support_15_19 = models.PositiveIntegerField('15 to 19', default=0)
    ovc_care_support_20_24 = models.PositiveIntegerField('20 to 24', default=0)
    ovc_care_support_25_plus = models.PositiveIntegerField('25 and above', default=0)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)
