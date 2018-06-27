-- views to "denormalize" data
-- apply with: 
-- psql nacmis -f views.sql

create or replace view vw_stakeholderdirectory as
  select st.*, pr.name as province_name, ds.name as district_name
  from data_entry_stakeholderdirectory st
  left outer join data_entry_province pr 
    on pr.id = st.organisation_province_id
  left outer join data_entry_district ds
    on ds.id = st.organisation_district_id; 

create or replace view vw_organisationtarget as
  select st.*, ot.organisation_target_option
  from data_entry_stakeholderdirectory_organisation_targets stot
  left outer join data_entry_organisationtarget ot 
    on ot.id = stot.organisationtarget_id
  left outer join vw_stakeholderdirectory st
    on st.id = stot.stakeholderdirectory_id;

create or replace view vw_activityreportform as
  select st.*, 
    arf.report_date as activityreportform_report_date, 
    arf.quarter_been_reported as activityreportform_quarter_been_reported, 
    arf.name as activityreportform_name,
    arf.telephone_number as activityreportform_telephone_number, 
    arf.email_address as activityreportform_email_address, 
    arf.id as activityreportform_id
  from data_entry_activityreportform arf
  left outer join vw_stakeholderdirectory st
    on st.id = arf.stake_holder_name_id;

-- join child tables with vw_activityreportform

create or replace view vw_condomprogramming as
  select ac.*,
    co.id as condomprogramming_id,
    co.condom_dist_point_num
  from data_entry_condomprogramming co
  left outer join vw_activityreportform ac
    on ac.activityreportform_id = co.activity_form_id;

create or replace view vw_condomprogramming2 as
  select ac.*,
    co.id as condomprogramming2_id,
    co.female_condom_distributed_num,
    co.male_condom_distributed_num
  from data_entry_condomprogramming2 co
  left outer join vw_activityreportform ac
    on ac.activityreportform_id = co.activity_form_id;

create or replace view vw_dacavalidation as
  select ac.*,
    dv.id as dacavalidation_id,
    dv.validation_date as dacavalidation_date,
    dv.form_validated,
    dv.validated_by_id
  from data_entry_dacavalidation dv
  left outer join vw_activityreportform ac
    on ac.activityreportform_id = dv.activity_form_id;

create or replace view vw_experiencedphysicalviolence as
  select ac.*,
    ex.id as experiencedphysicalviolence_id,
    ex.physical_female_less_10,
    ex.physical_female_10_14,
    ex.physical_female_15_19,
    ex.physical_female_20_24,
    ex.physical_female_25_plus,
    ex.physical_male_less_10,
    ex.physical_male_10_14,
    ex.physical_male_15_19,
    ex.physical_male_20_24,
    ex.physical_male_25_plus
  from data_entry_experiencedphysicalviolence ex
  left outer join vw_activityreportform ac
    on ac.activityreportform_id = ex.activity_form_id;
    
create or replace view vw_experiencedsexualviolence as
  select ac.*,
    ex.id as experiencedsexualviolence_id,
    ex.sexual_female_less_10,
    ex.sexual_female_10_14,
    ex.sexual_female_15_19,
    ex.sexual_female_20_24,
    ex.sexual_female_25_plus,
    ex.sexual_male_less_10,
    ex.sexual_male_10_14,
    ex.sexual_male_15_19,
    ex.sexual_male_20_24,
    ex.sexual_male_25_plus
  from data_entry_experiencedsexualviolence ex
  left outer join vw_activityreportform ac
    on ac.activityreportform_id = ex.activity_form_id;

create or replace view vw_iecmaterial as
  select ac.*,
    im.id as iecmaterial_id,
    im.material_type as iecmaterial_type,
    im.number_distributed as iecmaterial_number_distributed,
    im.localized as iecmaterial_localized
  from data_entry_iecmaterial im
  left outer join vw_activityreportform ac
    on ac.activityreportform_id = im.activity_form_id;

