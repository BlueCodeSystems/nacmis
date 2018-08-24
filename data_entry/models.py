from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.contrib.auth.models import User

from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

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
        return (self.name + ' - ' + self.district.name + ' district - '
        + self.district.province.name + ' province') 

#                       NATIONAL ORGANISATION
# *********************************************************************
class NationalOrganisation(models.Model):
    alphanumeric = RegexValidator(r'(?!^\d+$)^.+$', 'Only alphanumeric characters are allowed and not numbers only.')
    organisation_name = models.CharField(max_length=200, unique=True, validators=[alphanumeric])
    organisation_address = models.CharField('address of the organisation', max_length=100)
    organisation_contact_email = models.EmailField(max_length=254)

    def __str__(self):
        return self.organisation_name

    class Meta:
        verbose_name = 'parent organisation'

#               HELPER CLASSES FOR STAKEHOLDER DIRECTORY
# *********************************************************************

class OrganisationType(models.Model):
    organisation_type_option = models.CharField(max_length=100)

    def __str__(self):
        return self.organisation_type_option

class OrganisationTarget(models.Model):
    organisation_target_option = models.CharField('organisation target group', max_length=100, unique=True, default="")

    def __str__(self):
        return self.organisation_target_option

class PreventionMessageList(models.Model):
    prevention_message = models.CharField(max_length=100, unique=True, default="")
    
    def __str__(self):
        return self.prevention_message

#               HELPER CLASSES FOR ACTIVITYREPORTFORM 
# *********************************************************************
class MobilePopulationType(models.Model):
    mobile_population_type = models.CharField(max_length=100, unique=True, default="")

    def __str__(self):
        return self.mobile_population_type

#                   STAKEHOLDER DIRECTORY
# ************************************************************

class StakeholderDirectory(models.Model):

    # --> Basic details on the organisation
    national_organisation = models.ForeignKey(NationalOrganisation, verbose_name='parent organisation', on_delete=models.CASCADE, null=True)
    organisation = models.CharField('organisation/project', max_length=200, help_text='If organisation/project name is the same as \
        parent organisation. Please re-enter the same name')
    organisation_address = models.CharField('address of the organisation', max_length=100, blank=True, null=True)
    organisation_province = models.ForeignKey(Province, on_delete=models.CASCADE)
    organisation_district = models.ForeignKey(District, verbose_name='organisation district', on_delete=models.CASCADE)
    start_year = models.DateField('which year did your organisation start working in this district?')
    #start_year = models.IntegerField('which year did your organisation start working in this district?', 
        #validators=[MinValueValidator(1990, 'year value to low'), MaxValueValidator(2030, 'year value to high')], default="")
    gps = models.CharField('GPS Coordinates', help_text='use decimal degrees format(ie: -15.38753, 28.32282)', max_length=20, blank=True)
    website = models.URLField(max_length=200, blank=True)
    description_of_organisation = models.TextField('Brief description of the organisation (Please describe your \
        organisation in no more than 250 words)', max_length=1200)

    # --> Contact details
    key_contact_name = models.CharField('name of key contact person', max_length=50)
    position_within_organisation = models.CharField('position within the organisation', max_length=50)
    telephone_number = PhoneNumberField(help_text='09xxxxxxxx')
    telephone_number_alternative = PhoneNumberField(help_text='09xxxxxxxx', blank=True)
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
    other_organisation_type = models.CharField('other organisation/ group - please specify', max_length=100, null=True, blank=True)
    organisation_targets = models.ManyToManyField(OrganisationTarget, verbose_name='which group(s) does your organisation target? (please tick as many \
        different groups that are targeted by your organisation)')
    other_organisation_target = models.CharField('other target groups - please specify', max_length=100, null=True, blank=True)

    # --> Select HIV activities your organisation participates in
    
    iecmaterial = models.BooleanField('How many Information Education Communication (IEC) materials were distributed by \
        your organisation this quarter?', default=True)
    iecmaterial2 = models.BooleanField('If you distributed Information Education Communication (IEC) materials this \
        quarter who was your target audience?', default=True)
    teacher = models.BooleanField('Number of teachers who have received training, and taught lessons, in life skills \
        based comprehensive sexuality eduaction this quarter', default=True)
    outofschool = models.BooleanField('Number of Out of School children and young people aged 10-24 years provided \
        with life skills- based comprehensive sexuality education within this quarter', default=True)
    sexworker = models.BooleanField('How many sex workers were reached with HIV prevention programmes by your \
        organisation this quarter?', default=True)
    inmate = models.BooleanField('How many inmates were reached with HIV prevention programmes by your organisation \
        this quarter?', default=True)
    personswithdisability = models.BooleanField('How many persons with disability were reached with HIV prevention \
        programmes by your organisation this quarter?', default=True)
    mobileworker = models.BooleanField('How many mobile workers were reached with HIV prevention programmes by your \
        organisation this quarter?', default=True)
    mobilepopulation = models.BooleanField('Which types of mobile populations did your organisation reach this \
        quarter?', default=True)
    menwithmen = models.BooleanField('How many men who have sex with men (MSM) were reached with HIV prevention \
        programmes by your organisation this quarter?', default=True)
    transgenderindividual = models.BooleanField('How many transgender individuals were reached with HIV prevention \
        programmes by your organisation this quarter?', default=True)
    peoplewhoinjectdrug = models.BooleanField('How many people who inject drugs (PWID) have been reached by HIV \
        prevention programmes by your organisation this quarter?', default=True)
    condomprogramming = models.BooleanField('How many condom service distribution points were supplied by your \
        organisation this quarter (excluding health facilities)?', default=True)
    condomprogramming2 = models.BooleanField('How many male and/or female condoms were distributed to end users by \
        your organisation this quarter (excluding health facilities)?', default=True)
    reportedcase = models.BooleanField('What is the total number of reported cases on a physical or sexual violence \
        OR any other type of gender based violence by your organisation?', default=True)
    experiencedphysicalviolence = models.BooleanField('How many individuals experienced physical violence this \
        quarter?', default=True)
    experiencedsexualviolence = models.BooleanField('How many individuals experienced sexual violence this quarter?', 
        default=True)
    postexposureprophylaxis = models.BooleanField('How many individuals who experienced physical or sexual violence \
        were referred for post exposure prophylaxis(PEP) within 72 hours in accordance with national guidelines this \
        quarter?', default=True)
    preexposureprophylaxis = models.BooleanField('How many individuals were referred for pre-exposure \
        prophylaxis(PrEP) by your organisation this quarter?', default=True)
    synergydevelopmentsector = models.BooleanField('How many employees were reached through workplace programmes by \
        your organisation this quarter?', default=True)
    supportgroupsetup = models.BooleanField('How many support groups/ clubs/ after school groups set up by your \
        organisation were active this quarter?', default=True)
    individualcurrentlyenrolled = models.BooleanField('How many individuals are currently enrolled in support groups/ \
        clubs/ after school groups set up by your organisation this quarter?', default=True)
    vulnerablepeople = models.BooleanField('How many vulnerable people received care and support from your \
        organisation this quarter?', default=True)
    supportandcare = models.BooleanField('What types of care and support does your organisation provide? (select \
        all that apply)', default=True)
    
    def year_extract_in_start_year(self):
        year = self.start_year.strftime('%Y')
        return year
    year_extract_in_start_year.short_description = 'year organisation started'

    def __str__(self):
        return (self.organisation + ' - ' + self.organisation_district.name + ' district - '
        + self.organisation_district.province.name + ' province')
    
    class Meta:
        verbose_name_plural = 'Stakeholder Directory'

class UserProfile(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_by", editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    national_organisation = models.ForeignKey(NationalOrganisation, on_delete=models.CASCADE, null=True)
    stakeholder = models.ForeignKey(StakeholderDirectory, on_delete=models.SET_NULL, blank=True, null=True)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return "%s"%(self.user.username)
    
class SupportField(models.Model):
    area_of_support = models.CharField(max_length=100, unique=True, default="")

    def __str__(self):
        return self.area_of_support

class SourcesOfInformation(models.Model):
    source = models.CharField(max_length=100, unique=True, default="")

    def __str__(self):
        return self.source

    class Meta:
        verbose_name_plural = 'Sources of Information'

class ProgramActivity(models.Model):
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, null=True)
    areas_of_support = models.ManyToManyField(SupportField, verbose_name='Program activities by geographic area')
    organisation = models.ForeignKey(StakeholderDirectory, on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = ("ward", "organisation")

class FundingSource(models.Model):
    name_of_organisation =  models.CharField(max_length=100, default="")
    funding_amount = models.PositiveIntegerField('Funding Amount(In Zambian Kwacha)')
    organisation = models.ForeignKey(StakeholderDirectory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_of_organisation

    class Meta:
        unique_together = ("name_of_organisation", "organisation")

class TargetGroupPreventionMessage(models.Model):
    prevention_list = models.ManyToManyField(PreventionMessageList, verbose_name='prevention messages \
        conveyed by the program/ activity')
    target_groups = models.ManyToManyField(OrganisationTarget)
    other_organisation_target = models.CharField('other target groups - please specify', max_length=100, null=True, blank=True)
    organisation = models.ForeignKey(StakeholderDirectory, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.prevention_message

    #class Meta:
    #    unique_together = ("prevention_list", "organisation")

class TypesOfFundingSupport(models.Model):
    support_option =  models.CharField(max_length=100, default="")
    funding_source = models.ForeignKey(FundingSource, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.support_option

class OtherQuestion(models.Model):
    action_plan = models.CharField('Does you organisation have a current HIV and \
        AIDS action plan?', max_length=100, choices=YES_OR_NO);
    workplace_programme = models.CharField('Does your organisation have a current \
        and active HIV and AIDS workplace programme?', max_length=20, choices=YES_OR_NO)
    sources_of_information = models.ManyToManyField(SourcesOfInformation, verbose_name='which sources of \
        information does your organisation utilize to inform HIV programming and decision making?', )
    m_and_person = models.CharField('Does your organisation have a designated M and E person?', 
        max_length=20, choices=YES_OR_NO)
    organisation = models.ForeignKey(StakeholderDirectory, on_delete=models.CASCADE)

class EndOfYearQuestion(models.Model):
    funding = models.PositiveIntegerField('How much funding(in kwacha) was spent on HIV & \
        AIDS activities this year?')
    number_of_meetings_daft = models.PositiveIntegerField('How many DHAC meetings did your organisation attend \
        this year?')
    organisation = models.ForeignKey(StakeholderDirectory, on_delete=models.CASCADE)

class GeneralComment(models.Model):
    general_comment = models.TextField('Additional Comments', blank=True)
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
    telephone_number = PhoneNumberField(help_text='0xxxxxxxxx')
    email_address = models.EmailField(max_length=50)
    '''
    def year_quarter_tuple(self):
        return (("201801", "2018 - quarter 1"), ("201802", "2018 - quarter 2"), 
            ("201803", "2018 - quarter 3"), ("201804", "2018 - quarter 4"))
    '''

    def __str__(self):
        if self.stake_holder_name:
            return self.stake_holder_name.organisation + " - " + self.quarter_been_reported
        else:
            return "unset stakeholder name"

    class Meta:
        verbose_name_plural = 'Stakeholder Activity Report Form (SARF)'

VALIDATION_STATUS = (
    ('submitted', 'Submitted'),
    ('needs_review', 'Needs Review'),
    ('approved', 'Approved'),
)

STAKEHOLDER_ACKNOWLEDGEMENT_STATEMENT = """ I verify that this information is complete and correct and that I have not 
    misrepresented any information."""
    
DACA_ACKNOWLEDGEMENT_STATEMENT = """I acknowledge that I have validated this SARF for data accuracy to the best of my ability. 
                             Any necessary corrections were discussed with the stakeholder prior to this approval. 
                  
                             Please type your initials below as acknowledgement of the above statement"""

class StakeholderVerification(models.Model):
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.SET_NULL, null=True)
    acknowledgement = models.TextField(max_length=1200, default=STAKEHOLDER_ACKNOWLEDGEMENT_STATEMENT)
    stakeholder_initials = models.CharField('initials', max_length=5)

class DACAValidation(models.Model):
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.SET_NULL, null=True)
    validation_date = models.DateTimeField('Validation Date', auto_now=True)
    validated_by = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Validated By', null=True)
    validation_status = models.CharField('DACA validation status', max_length=15, choices=VALIDATION_STATUS)
    acknowledgement = models.TextField(max_length=1200, default=DACA_ACKNOWLEDGEMENT_STATEMENT)
    daca_initials = models.CharField('DACA Initials', max_length=5)#We will add the validation statement as read only from the admin.
    validation_comment = models.TextField('Validation Comment', max_length=600, null=True, blank=True)

    def __str__(self):
        return self.validation_status
   
class PITMEOValidation(models.Model):
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.SET_NULL, null=True)
    validation_date = models.DateTimeField('Validation Date', auto_now=True)
    validated_by = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Validated By', null=True)
    validation_status = models.CharField('PITMEO validation status', max_length=15, choices=VALIDATION_STATUS)
    acknowledgement = models.TextField(max_length=1200, default=DACA_ACKNOWLEDGEMENT_STATEMENT)
    pitmeo_initials = models.CharField('PITMEO Initials', max_length=5)
    validation_comment = models.TextField('Validation Comment', max_length=600, null=True, blank=True)

    def __str__(self):
        return self.validation_status
  
# --> Social behaviour change communication 
class IECMaterial(models.Model):
    material_type = models.CharField('type of IEC material', max_length=100, choices=IEC_MATERIALS)
    number_distributed = models.PositiveIntegerField('number distributed', null=True)
    localized = models.BooleanField('localised', default=False)
    activity_form = models.ForeignKey(ActivityReportForm, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.material_type

    class Meta:
        unique_together = ("material_type", "activity_form")

class IECMaterial2(models.Model):
    target_audience = models.ManyToManyField(OrganisationTarget)
    other_target_audience = models.CharField('other', max_length=100, null=True, blank=True)
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
        other_mobile_population = models.CharField('other', max_length=100, null=True, blank=True)
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
    general_comment = models.TextField('Additional Comment', help_text='Please share any additional comments \
        or details about your stakeholder activity report form for this (SARF)', blank=True)
    organisation = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

    def __str__(self):
        return ''
    
    class Meta:
        verbose_name = 'additional comment'
# Subheader for Question 2 in ActivityReportForm
class SubheaderLabel1(models.Model):
    organisation = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class SubheaderLabel2(models.Model):
    organisation = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class SubheaderLabel3(models.Model):
    organisation = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class SubheaderLabel4(models.Model):
    organisation = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class SubheaderLabel5(models.Model):
    organisation = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class SubheaderLabel6(models.Model):
    organisation = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)

class SubheaderLabel7(models.Model):
    organisation = models.ForeignKey(ActivityReportForm, on_delete=models.CASCADE)
