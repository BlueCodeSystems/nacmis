from phonenumber_field.modelfields import PhoneNumberField

from django.db import models

# Create your models here.
# list variables
cbo = 'Community Based Organisation'
fbo = 'Faith Based Organisation'
local_ngo = 'Local NGO'
inter_ngo = 'International NGO'
government = 'Government Organisation'
private = 'Private Organisation'
org_others = 'Other organisation / group - please specify'

lusaka = 'Lusaka'
central = 'Central'
copperbelt = 'Copperbelt'
eastern = 'Eastern'
luapula = 'Luapula'
muchinga = 'Muchinga'
north_western = 'North Westen'
northern = 'Northern'
southern = 'Southern'
western = 'Western'

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

truck_driver = 'Long distance truck drivers'
fish_traders = 'Fish traders'
miners = 'Miners'
cross_boarder_traders = 'Cross-border traders'
seasonal_workers = 'Seasonal workers (plantations, farming, etc.)'
contruction_workers = 'Construction workers'
mobile_others = 'Others'

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

ORGANISATION_TYPE_LIST = (
    (cbo, 'Community Based Organisation'),
    (fbo, 'Faith Based Organisation'),
    (government, 'Government Organisation'),
    (inter_ngo, 'International Non Governmental Organisation'),
    (local_ngo, 'Local Non Governmental Organisation'),
    (private, 'Private Organisation'),
    (org_others, 'Other organisation / group - please specify')
)

PROVINCES_ZAMBIA = (
    (lusaka, 'Lusaka'),
    (central, 'Central'),
    (copperbelt, 'Copperbelt'),
    (eastern, 'Eastern'),
    (luapula, 'Luapula'),
    (muchinga, 'Muchinga'),
    (north_western, 'North Western'),
    (northern, 'Northern'),
    (southern, 'Southern'),
    (western, 'Western')
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
    ),
    (
        'Mpongwe', (
            ('Ibenga', 'Ibenga'),
            ('Munkumpu', 'Munkumpu')
        )
    )
)  

ORGANISATION_TARGET_LIST = (
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

TYPE_OF_MOBILE_POPULATION = (
    (truck_driver, 'Long distance truck drivers'),
    (fish_traders, 'Fish traders'),
    (miners, 'Miners'),
    (cross_boarder_traders, 'Cross-border traders'),
    (seasonal_workers, 'Seasonal workers (plantations, farming, etc.)'),
    (contruction_workers, 'Construction workers'),
    (mobile_others, 'Others')
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

class Province(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class District(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Ward(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#                       NATIONAL ORGANISATION
# *********************************************************************
class NationalOrganisation(models.Model):
    organisation_name = models.CharField(max_length=200)
    organisation_address = models.CharField('address of the organisation', max_length=100)
    organisation_contact_email = models.EmailField(max_length=254)

    def __str__(self):
        return self.organisation_name + " - " + self.organisation_contact_email

#               HELPER CLASSES FOR STAKEHOLDER DIRECTORY
# *********************************************************************

class OrganisationType(models.Model):
    organisation_type_option = models.CharField(max_length=100)

    def __str__(self):
        return self.organisation_type_option

class OrganisationTarget(models.Model):
    organisation_target_option = models.CharField('organisation target group', max_length=100, default="")

    def __str__(self):
        return self.organisation_target_option

#               HELPER CLASSES FOR ACTIVITYREPORTFORM 
# *********************************************************************
class MobilePopulationType(models.Model):
    mobile_population_type = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.mobile_population_type


#                   STAKEHOLDER DIRECTORY
# ************************************************************

class StakeholderDirectory(models.Model):

    class Meta:
        verbose_name_plural = 'Stakeholder directories'

    # --> Basic details on the organisation
    national_organisation = models.ForeignKey(NationalOrganisation, on_delete=models.CASCADE, null=True)
    organisation = models.CharField(max_length=200)
    organisation_address = models.CharField('address of the organisation', max_length=100, blank=True, null=True)
    organisation_province = models.ForeignKey(Province, on_delete=models.CASCADE, null=True)
    organisation_district = models.ForeignKey(District, verbose_name='organisation district', on_delete=models.CASCADE, null=True)
    start_year = models.DateField('which year did your organisation start working in this district?')
    gps = models.CharField('GPS Coordinates', max_length=20, blank=True)
    website = models.URLField(max_length=200, blank=True)
    description_of_organisation = models.TextField('Brief description of the organisation (Please describe your \
        organisation in no more than 250 words)')

    # --> Contact details
    key_contact_name = models.CharField('name of key contact person', max_length=50)
    position_within_organisation = models.CharField('position within the organisation', max_length=50)
    telephone_number = PhoneNumberField()
    telephone_number_alternative = PhoneNumberField(blank=True)
    email_address = models.EmailField('email address', max_length=254)

    # --> Staff details
    permanent_employee_female = models.PositiveIntegerField('current number of permanent female employees', null=True)
    permanent_employee_male = models.PositiveIntegerField('current number of permanent male employees', null=True)
    temporary_employee_female = models.PositiveIntegerField('current number of temporary female employees', null=True)
    temporary_employee_male = models.PositiveIntegerField('current number of temporary male employees', null=True)
    volunteer_employee_female = models.PositiveIntegerField('current number of volunteer female employees', null=True)
    volunteer_employee_male = models.PositiveIntegerField('current number of volunteer male employees', null=True)

    # --> Organisation Classification
    organisation_type = models.CharField('which of the following \'types\' would best describe your \
        organisation? (Please only tick one type of organisation)', max_length=100, choices=ORGANISATION_TYPE_LIST)
    organisation_targets = models.ManyToManyField(OrganisationTarget, verbose_name='which group(s) does your organisation target? (please tick as many \
        different groups that are targeted by your organisation)')

    def __str__(self):
        return (self.organisation + ' - ' + self.organisation_district.name + ' district - '
        + self.organisation_district.province.name + ' province') 

class SupportField(models.Model):
    area_of_support = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.area_of_support

class ProgramActivity(models.Model):
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, null=True)
    areas_of_support = models.ManyToManyField(SupportField, verbose_name='Program activities by geographic area')
    organisation = models.ForeignKey(StakeholderDirectory, on_delete=models.SET_NULL, null=True)

class FundingSource(models.Model):
    name_of_organisation =  models.CharField(max_length=100, default="")
    funding_amount =  models.PositiveIntegerField('Funding Amount(In US Dollars)')
    organisation = models.ForeignKey(StakeholderDirectory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_of_organisation

class TargetGroupPreventionMessage(models.Model):
    prevention_message = models.CharField(max_length=100, choices=PREVENTION_MESSAGES_LIST, null=True)
    target_groups = models.ManyToManyField(OrganisationTarget)
    organisation = models.ForeignKey(StakeholderDirectory, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        #return self.target_group + " " + self.prevention_message
        return self.prevention_message

class TypesOfFundingSupport(models.Model):
    support_option =  models.CharField(max_length=100, default="")
    funding_source = models.ForeignKey(FundingSource, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.support_option

class OtherQuestion(models.Model):
    action_plan = models.CharField('Does you organisation hava a current HIV and \
        AIDS action plan?', max_length=100, choices=YES_OR_NO);
    workplace_programme = models.CharField('Does your organisation have a current \
        and active HIV and AIDS workplace programme?', max_length=20, choices=YES_OR_NO)
    sources_of_information = models.CharField('which sources of information does your \
        organisation utilize to inform HIV programming and decision making?', max_length=20,
        choices=SOURCES_OF_INFORMATION)
    m_and_person = models.CharField('Does your organisation have a designated M and E person?', 
        max_length=20, choices=YES_OR_NO)
    organisation = models.ForeignKey(StakeholderDirectory, on_delete=models.CASCADE)

class EndOfYearQuestion(models.Model):
    funding = models.PositiveIntegerField('How much funding(in kwacha) was spent on HIV & \
        AIDS activities this year?')
    number_of_meetings_daft = models.PositiveIntegerField('How many DATF meetings did your organisation attend \
        this year?')
    number_of_meetings_paft = models.PositiveIntegerField('How many PATF meetings did your organisation attend \
        this year?')
    organisation = models.ForeignKey(StakeholderDirectory, on_delete=models.CASCADE)

class GeneralComment(models.Model):
    general_comment = models.TextField('additional comments', blank=True)
    organisation = models.ForeignKey(StakeholderDirectory, on_delete=models.CASCADE)

    def __str__(self):
        return ''

    class Meta:
        verbose_name = 'additional comment'

# HIV ACTIVITIES ORGANISATION PARTICIPATES IN FORM
# *************************************************
    
class ActivityReportForm(models.Model):

    report_date = models.DateField(null=True)
    quarter_been_reported = models.CharField(verbose_name='quarter being reported', max_length=20, choices=QUARTER_LIST)
    stake_holder_name = models.ForeignKey(StakeholderDirectory, verbose_name='Name of the Organisation', \
        on_delete=models.SET_NULL, null=True)
    
    # Location and Report Compilation section
    name = models.CharField(max_length=50)
    telephone_number = PhoneNumberField()
    email_address = models.EmailField(max_length=50)

    def __str__(self):
        if self.stake_holder_name:
            return self.stake_holder_name.organisation + " - " + self.quarter_been_reported
        else:
            return "unset stakeholder name"

# --> Social behaviour change communication 
class IECMaterial(models.Model):
    material_type = models.CharField('type of IEC material', max_length=100, choices=IEC_MATERIALS)
    number_distributed = models.PositiveIntegerField('number distributed', null=True)
    localized = models.BooleanField('number localised', default=False)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.material_type

class IECMaterial2(models.Model):
    target_audience = models.ManyToManyField(OrganisationTarget)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return 'IEC audience'

# --> Social behaviour change communication for key populations 
class Teachers(models.Model):
    teachers_female = models.PositiveIntegerField('female', null=True)
    teachers_male = models.PositiveIntegerField('male', null=True)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)
    
class OutOfSchool(models.Model):
    out_school_female_10_14 = models.PositiveIntegerField('female 10 to 14', null=True)
    out_school_female_15_19 = models.PositiveIntegerField('female 15 to 19', null=True)
    out_school_female_20_24 = models.PositiveIntegerField('female 20 to 24', null=True)

    out_school_male_10_14 = models.PositiveIntegerField('male 10 to 14', null=True)
    out_school_male_15_19 = models.PositiveIntegerField('male 15 to 19', null=True)
    out_school_male_20_24 = models.PositiveIntegerField('male 20 to 24', null=True)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class SexWorker(models.Model):
    sex_workers_female_10_14 = models.PositiveIntegerField('female 10 to 14', null=True)
    sex_workers_female_15_19 = models.PositiveIntegerField('female 15 to 19', null=True)
    sex_workers_female_20_24 = models.PositiveIntegerField('female 20 to 24', null=True)
    sex_workers_female_25_29 = models.PositiveIntegerField('female 25 to 29', null=True)
    sex_workers_female_30_34 = models.PositiveIntegerField('female 30 to 34', null=True)
    sex_workers_female_35_plus = models.PositiveIntegerField('female 35 plus', null=True)

    sex_workers_male_10_14 = models.PositiveIntegerField('male 10 to 14', null=True)
    sex_workers_male_15_19 = models.PositiveIntegerField('male 15 to 19', null=True)
    sex_workers_male_20_24 = models.PositiveIntegerField('male 20 to 24', null=True)
    sex_workers_male_25_29 = models.PositiveIntegerField('male 25 to 29', null=True)
    sex_workers_male_30_34 = models.PositiveIntegerField('male 30 to 34', null=True)
    sex_workers_male_35_plus = models.PositiveIntegerField('male 35 plus', null=True)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)
 
class Inmate(models.Model):
    inmates_female_num = models.PositiveIntegerField('female', null=True)
    inmates_male_num = models.PositiveIntegerField('male', null=True)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class PersonsWithDisabilty(models.Model):
    pwd_female_num = models.PositiveIntegerField('females', null=True)
    pwd_male_num = models.PositiveIntegerField('males', null=True)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class MobileWorker(models.Model):
    mobile_workers_female_num = models.PositiveIntegerField('female', null=True)
    mobile_workers_male_num = models.PositiveIntegerField('male', null=True)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class MobilePopulation(models.Model):
        mobile_population_types = models.ManyToManyField(MobilePopulationType)
        activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE, null=True)

class MenWithMen(models.Model):
    men_with_men = models.PositiveIntegerField('number', null=True)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class TransgenderIndividual(models.Model):
    transgender_num = models.PositiveIntegerField('number', null=True)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class PeopleWhoInjectDrug(models.Model):
    pwid_female = models.PositiveIntegerField('female', null=True)
    pwid_male = models.PositiveIntegerField('male', null=True)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

# Condom Programming
class CondomProgramming(models.Model):
    condom_dist_point_num = models.PositiveIntegerField('number', null=True)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class CondomProgramming2(models.Model):
    female_condom_distributed_num = models.PositiveIntegerField('female', null=True)
    male_condom_distributed_num = models.PositiveIntegerField('male', null=True)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

# Critical Enablers
class ReportedCase(models.Model):
    reported_female_less_10 = models.PositiveIntegerField('female less than 10', null=True)
    reported_female_10_14 = models.PositiveIntegerField('female 10 to 14', null=True)
    reported_female_15_19 = models.PositiveIntegerField('female 15 to 19', null=True)
    reported_female_20_24 = models.PositiveIntegerField('female 20 to 24', null=True)
    reported_female_25_plus = models.PositiveIntegerField('female 25 plus', null=True)

    reported_male_less_10 = models.PositiveIntegerField('male less than 10', null=True)
    reported_male_10_14 = models.PositiveIntegerField('male 10 to 14', null=True)
    reported_male_15_19 = models.PositiveIntegerField('male 15 to 19', null=True)
    reported_male_20_24 = models.PositiveIntegerField('male 20 to 24', null=True)
    reported_male_25_plus = models.PositiveIntegerField('male 25 plus', null=True)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class ExperiencedPhysicalViolence(models.Model):
    physical_female_less_10 = models.PositiveIntegerField('female less than 10', null=True)
    physical_female_10_14 = models.PositiveIntegerField('female 10 to 14', null=True)
    physical_female_15_19 = models.PositiveIntegerField('female 15 to 19', null=True)
    physical_female_20_24 = models.PositiveIntegerField('female 20 to 24', null=True)
    physical_female_25_plus = models.PositiveIntegerField('female 25 plus', null=True)

    physical_male_less_10 = models.PositiveIntegerField('male less than 10', null=True)
    physical_male_10_14 = models.PositiveIntegerField('male 10 to 14', null=True)
    physical_male_15_19 = models.PositiveIntegerField('male 15 to 19', null=True)
    physical_male_20_24 = models.PositiveIntegerField('male 20 to 24', null=True)
    physical_male_25_plus = models.PositiveIntegerField('male 25 plus', null=True)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class ExperiencedSexualViolence(models.Model):
    sexual_female_less_10 = models.PositiveIntegerField('female less than 10', null=True)
    sexual_female_10_14 = models.PositiveIntegerField('female 10 to 14', null=True)
    sexual_female_15_19 = models.PositiveIntegerField('female 15 to 19', null=True)
    sexual_female_20_24 = models.PositiveIntegerField('female 20 to 24', null=True)
    sexual_female_25_plus = models.PositiveIntegerField('female 25 plus', null=True)

    sexual_male_less_10 = models.PositiveIntegerField('male less than 10', null=True)
    sexual_male_10_14 = models.PositiveIntegerField('male 10 to 14', null=True)
    sexual_male_15_19 = models.PositiveIntegerField('male 15 to 19', null=True)
    sexual_male_20_24 = models.PositiveIntegerField('male 20 to 24', null=True)
    sexual_male_25_plus = models.PositiveIntegerField('male 25 plus', null=True)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class PostExposureProphylaxis(models.Model):
    accessed_pep_female_less_10 = models.PositiveIntegerField('female less than 10', null=True)
    accessed_pep_female_10_14 = models.PositiveIntegerField('female 10 to 14', null=True)
    accessed_pep_female_15_19 = models.PositiveIntegerField('female 15 to 19', null=True)
    accessed_pep_female_20_24 = models.PositiveIntegerField('female 20 to 24', null=True)
    accessed_pep_female_25_plus = models.PositiveIntegerField('female 25 plus', null=True)

    accessed_pep_male_less_10 = models.PositiveIntegerField('male less than 10', null=True)
    accessed_pep_male_10_14 = models.PositiveIntegerField('male 10 to 14', null=True)
    accessed_pep_male_15_19 = models.PositiveIntegerField('male 15 to 19', null=True)
    accessed_pep_male_20_24 = models.PositiveIntegerField('male 20 to 24', null=True)
    accessed_pep_male_25_plus = models.PositiveIntegerField('male 25 plus', null=True)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class PreExposureProphylaxis(models.Model):
    referred_pep_female_15_19 = models.PositiveIntegerField('female 15 to 19', null=True)
    referred_pep_female_20_24 = models.PositiveIntegerField('female 20 to 24', null=True)
    referred_pep_female_25_plus = models.PositiveIntegerField('female 25 plus', null=True)

    referred_pep_male_15_19 = models.PositiveIntegerField('male 15 to 19', null=True)
    referred_pep_male_20_24 = models.PositiveIntegerField('male 20 to 24', null=True)
    referred_pep_male_25_plus = models.PositiveIntegerField('male 25 plus', null=True)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

# Synergies with other development sectors
class SynergyDevelopmentSector(models.Model):
    employees_reached_female_num = models.PositiveIntegerField('female', null=True)
    employees_reached_male_num = models.PositiveIntegerField('male', null=True)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class SupportGroupSetUp(models.Model):
    support_groups = models.PositiveIntegerField('number', null=True)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class IndividualCurrentlyEnrolled(models.Model):
    individuals_enrolled_female_10_14 = models.PositiveIntegerField('female 10 to 14', null=True)
    individuals_enrolled_female_15_19 = models.PositiveIntegerField('female 15 to 19', null=True)
    individuals_enrolled_female_20_24 = models.PositiveIntegerField('female 20 to 24', null=True)
    individuals_enrolled_female_25_plus = models.PositiveIntegerField('female 25 plus', null=True)

    individuals_enrolled_male_10_14 = models.PositiveIntegerField('male 10 to 14', null=True)
    individuals_enrolled_male_15_19 = models.PositiveIntegerField('male 15 to 19', null=True)
    individuals_enrolled_male_20_24 = models.PositiveIntegerField('male 20 to 24', null=True)
    individuals_enrolled_male_25_plus = models.PositiveIntegerField('male 25 plus', null=True)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class VulnerablePeople(models.Model):
    ovc_female_less_10 = models.PositiveIntegerField('female less than 10', null=True)
    ovc_female_10_14 = models.PositiveIntegerField('female 10 to 14', null=True)
    ovc_female_15_19 = models.PositiveIntegerField('female 15 to 19', null=True)
    ovc_female_20_24 = models.PositiveIntegerField('female 20 to 24', null=True)
    ovc_female_25_plus = models.PositiveIntegerField('female 25 plus', null=True)

    ovc_male_less_10 = models.PositiveIntegerField('male less than 10',null=True)
    ovc_male_10_14 = models.PositiveIntegerField('male 10 to 14',null=True)
    ovc_male_15_19 = models.PositiveIntegerField('male 15 to 19',null=True)
    ovc_male_20_24 = models.PositiveIntegerField('male 20 to 24',null=True)
    ovc_male_25_plus = models.PositiveIntegerField('male 25 plus',null=True)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class SupportAndCare(models.Model):
    type = models.ManyToManyField(SupportField, verbose_name='type')
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class GeneralComment2(models.Model):
    general_comment = models.TextField('additional comment', blank=True)
    organisation = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

    def __str__(self):
        return ''
    
    class Meta:
        verbose_name = 'additional comment'
