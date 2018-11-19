-- views to "denormalize" data
-- apply with: 
-- psql nacmis -f views.sql

create or replace view vw_stakeholderdirectory as
 select st.*, pr.name as province_name,  ds.district_longitude, ds.district_latitude, ds.name as district_name
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

drop view if exists vw_activityreportform CASCADE;
create or replace view vw_activityreportform as
  select st.*, 
    arf.report_date as activityreportform_report_date,
    CASE 
      WHEN (arf.quarter_been_reported ~ '\d{4}01') THEN 'Q1 '||substring(arf.quarter_been_reported, 1, 4)
      WHEN (arf.quarter_been_reported ~ '\d{4}02') THEN 'Q2 '||substring(arf.quarter_been_reported, 1, 4)
      WHEN (arf.quarter_been_reported ~ '\d{4}03') THEN 'Q3 '||substring(arf.quarter_been_reported, 1, 4)
      WHEN (arf.quarter_been_reported ~ '\d{4}04') THEN 'Q4 '||substring(arf.quarter_been_reported, 1, 4)
      ELSE arf.quarter_been_reported
    END AS activityreportform_quarter_been_reported,
    arf.name as activityreportform_name,
    arf.telephone_number as activityreportform_telephone_number, 
    arf.email_address as activityreportform_email_address, 
    arf.id as activityreportform_id
  from data_entry_activityreportform arf
  left outer join vw_stakeholderdirectory st
    on st.id = arf.stake_holder_name_id
  WHERE arf.quarter_been_reported >= '201801';

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

drop view if exists vw_dacavalidation;
create or replace view vw_dacavalidation as
  select ac.*,
    dv.id as dacavalidation_id,
    dv.validation_date as dacavalidation_date,
    dv.validation_status,
    dv.acknowledgement,
    dv.daca_initials,
    dv.validation_comment,
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

 CREATE OR REPLACE VIEW vw_iecmaterial_target_audience as select
    vw_activityreportform.*,
    activity_form_id,
    data_entry_iecmaterial2.id as iecmaterial2_id,
    organisationtarget_id,
    organisation_target_option
  from data_entry_iecmaterial2
  left outer JOIN data_entry_iecmaterial2_target_audience
    on iecmaterial2_id = data_entry_iecmaterial2_target_audience.iecmaterial2_id
  left outer JOIN data_entry_organisationtarget
    on organisationtarget_id = data_entry_organisationtarget.id
  left outer JOIN vw_activityreportform
    on activity_form_id = vw_activityreportform.id;
 
drop view if exists vw_individualcurrentlyenrolled;
create or replace view vw_individualcurrentlyenrolled as
  select ac.*,
    ice.id as individualcurrentlyenrolled_id,
    ice.individuals_enrolled_female_10_14,
    ice.individuals_enrolled_female_15_19,
    ice.individuals_enrolled_female_20_24,
    ice.individuals_enrolled_female_25_plus,
    ice.individuals_enrolled_male_10_14,
    ice.individuals_enrolled_male_15_19,
    ice.individuals_enrolled_male_20_24,
    ice.individuals_enrolled_male_25_plus
  from data_entry_individualcurrentlyenrolled ice
  left outer join vw_activityreportform ac
    on ac.activityreportform_id = ice.activity_form_id;

create or replace view vw_inmate as
  select ac.*,
    im.id as inmate_id,
    im.inmates_female_num,
    im.inmates_male_num
  from data_entry_inmate im
  left outer join vw_activityreportform ac
    on ac.activityreportform_id = im.activity_form_id;

create or replace view vw_menwithmen as
  select ac.*,
    mm.id as menwithmen_id,
    mm.men_with_men
  from data_entry_menwithmen mm
  left outer join vw_activityreportform ac
    on ac.activityreportform_id = mm.activity_form_id;

create or replace view vw_mobilepopulation as
  select ac.*,
    mp.id as mobilepopulation_id
  from data_entry_mobilepopulation mp
  left outer join vw_activityreportform ac
    on ac.activityreportform_id = mp.activity_form_id;

create or replace view vw_mobileworker as
  select ac.*,
    mw.id as mobileworker_id,
    mw.mobile_workers_female_num,
    mw.mobile_workers_male_num
  from data_entry_mobileworker mw
  left outer join vw_activityreportform ac
    on ac.activityreportform_id = mw.activity_form_id;

create or replace view vw_outofschool as
  select ac.*,
    oos.id as outofschool_id,
    oos.out_school_female_10_14,
    oos.out_school_female_15_19,
    oos.out_school_female_20_24,
    oos.out_school_male_10_14,
    oos.out_school_male_15_19,
    oos.out_school_male_20_24
  from data_entry_outofschool oos
  left outer join vw_activityreportform ac
    on ac.activityreportform_id = oos.activity_form_id;

create or replace view vw_peoplewhoinjectdrug as
  select ac.*,
    pd.id as peoplewhoinjectdrug_id,
    pd.pwid_female,
    pd.pwid_male
  from data_entry_peoplewhoinjectdrug pd
  left outer join vw_activityreportform ac
    on ac.activityreportform_id = pd.activity_form_id;

create or replace view vw_personswithdisability as
  select ac.*,
    pd.id as personswithdisability_id,
    pd.pwd_female_num,
    pd.pwd_male_num
  from data_entry_personswithdisabilty pd
  left outer join vw_activityreportform ac
    on ac.activityreportform_id = pd.activity_form_id;

create or replace view vw_postexposureprophylaxis as
  select ac.*,
    pp.id as postexposureprophylaxis_id,
    pp.accessed_pep_female_less_10,
    pp.accessed_pep_female_10_14,
    pp.accessed_pep_female_15_19,
    pp.accessed_pep_female_20_24,
    pp.accessed_pep_female_25_plus,
    pp.accessed_pep_male_less_10,
    pp.accessed_pep_male_10_14,
    pp.accessed_pep_male_15_19,
    pp.accessed_pep_male_20_24,
    pp.accessed_pep_male_25_plus
  from data_entry_postexposureprophylaxis pp
  left outer join vw_activityreportform ac
    on ac.activityreportform_id = pp.activity_form_id;

create or replace view vw_preexposureprophylaxis as
  select ac.*,
    pp.id as preexposureprophylaxis_id,
    pp.referred_pep_female_15_19,
    pp.referred_pep_female_20_24,
    pp.referred_pep_female_25_plus,
    pp.referred_pep_male_15_19,
    pp.referred_pep_male_20_24,
    pp.referred_pep_male_25_plus
  from data_entry_preexposureprophylaxis pp
  left outer join vw_activityreportform ac
    on ac.activityreportform_id = pp.activity_form_id;

create or replace view vw_reportedcase as
  select ac.*,
    rc.id as reportedcase_id,
    rc.reported_female_less_10,
    rc.reported_female_10_14,
    rc.reported_female_15_19,
    rc.reported_female_20_24,
    rc.reported_female_25_plus,
    rc.reported_male_less_10,
    rc.reported_male_10_14,
    rc.reported_male_15_19,
    rc.reported_male_20_24,
    rc.reported_male_25_plus
  from data_entry_reportedcase rc
  left outer join vw_activityreportform ac
    on ac.activityreportform_id = rc.activity_form_id;

create or replace view vw_sexworker as
  select ac.*,
    sw.id as sexworker_id,
    sw.sex_workers_female_10_14,
    sw.sex_workers_female_15_19,
    sw.sex_workers_female_20_24,
    sw.sex_workers_female_25_29,
    sw.sex_workers_female_30_34,
    sw.sex_workers_female_35_plus,
    sw.sex_workers_male_10_14,
    sw.sex_workers_male_15_19,
    sw.sex_workers_male_20_24,
    sw.sex_workers_male_25_29,
    sw.sex_workers_male_30_34,
    sw.sex_workers_male_35_plus
  from data_entry_sexworker sw
  left outer join vw_activityreportform ac
    on ac.activityreportform_id = sw.activity_form_id;

create or replace view vw_supportandcare as
  select ac.*,
    sc.id as supportandcare_id
  from data_entry_supportandcare sc
  left outer join vw_activityreportform ac
    on ac.activityreportform_id = sc.activity_form_id;

create or replace view vw_supportgroupsetup as
  select ac.*,
    s.id as supportgroupsetup_id,
    s.support_groups
  from data_entry_supportgroupsetup s
  left outer join vw_activityreportform ac
    on ac.activityreportform_id = s.activity_form_id;

create or replace view vw_synergydevelopmentsector as
  select ac.*,
    s.id as synergydevelopmentsector_id,
    s.employees_reached_female_num,
    s.employees_reached_male_num
  from data_entry_synergydevelopmentsector s
  left outer join vw_activityreportform ac
    on ac.activityreportform_id = s.activity_form_id;

create or replace view vw_teachers as
  select ac.*,
    t.id as teachers_id,
    t.teachers_female,
    t.teachers_male
  from data_entry_teachers t
  left outer join vw_activityreportform ac
    on ac.activityreportform_id = t.activity_form_id;

create or replace view vw_transgenderindividual as
  select ac.*,
    t.id as transgenderindividual_id,
    t.transgender_num
  from data_entry_transgenderindividual t
  left outer join vw_activityreportform ac
    on ac.activityreportform_id = t.activity_form_id;

create or replace view vw_vulnerablepeople as
  select ac.*,
    vp.id as vulnerablepeople_id,
    vp.ovc_female_10_14,
    vp.ovc_female_15_19,
    vp.ovc_female_20_24,
    vp.ovc_female_25_plus,
    vp.ovc_male_10_14,
    vp.ovc_male_15_19,
    vp.ovc_male_20_24,
    vp.ovc_male_25_plus
  from data_entry_vulnerablepeople vp
  left outer join vw_activityreportform ac
    on ac.activityreportform_id = vp.activity_form_id;

-- join with vw_organisationtarget

/*create or replace view vw_endofyearquestion as
  select o.*,
    q.funding,
    q.number_of_meetings_daft,
    q.number_of_meetings_paft,
    q.id as endofyearquestion_id
  from data_entry_endofyearquestion q
  left outer join vw_organisationtarget o 
    on o.id = q.organisation_id;
*/

create or replace view vw_fundingsource as
  select o.*,
    f.name_of_organisation,
    f.funding_amount,
    f.id as fundingsource_id
  from data_entry_fundingsource f
  left outer join vw_organisationtarget o
    on o.id = f.organisation_id;

create or replace view vw_generalcomment as
  select o.*,
    g.general_comment,
    g.id as generalcomment_id
  from data_entry_generalcomment g
  left outer join vw_organisationtarget o
    on o.id = g.organisation_id;

create or replace view vw_generalcomment2 as
  select o.*,
    g.general_comment,
    g.id as generalcomment_id
  from data_entry_generalcomment2 g
  left outer join vw_organisationtarget o
    on o.id = g.organisation_id;

/*create or replace view vw_otherquestion as
  select o.*,
    oq.action_plan,
    oq.workplace_programme,
    oq.sources_of_information,
    oq.m_and_person,
    oq.id as otherquestion_id
  from data_entry_otherquestion oq
  left outer join vw_organisationtarget o
    on o.id = oq.organisation_id;
*/

create or replace view vw_programactivity as
  select o.*,
    p.id as programactivity_id,
    w.name as ward_name
  from data_entry_programactivity p
  left outer join vw_organisationtarget o
    on o.id = p.organisation_id
  left outer join data_entry_ward w
    on p.ward_id = w.id;
/*
create or replace view vw_targetgrouppreventionmessage as
  select o.*,
    t.id as targetgrouppreventionmessage_id,
    t.prevention_message
  from data_entry_targetgrouppreventionmessage t
  left outer join vw_organisationtarget o
    on o.id = t.organisation_id;
*/
drop view if exists vw_mobilepopulation_types;
create or replace view vw_mobilepopulation_types as
  select mp.*,
    m2m_mobile_types.id as m2m_id,
    mpt.mobile_population_type,
    m2m_mobile_types.mobilepopulationtype_id
  from data_entry_mobilepopulation_mobile_population_types m2m_mobile_types
  left outer join vw_mobilepopulation mp on mp.mobilepopulation_id = m2m_mobile_types.mobilepopulation_id
  left outer join data_entry_mobilepopulationtype mpt on mpt.id = m2m_mobile_types.mobilepopulationtype_id;

-- stored procedures

-- pick apart the data_entry_sexworker table, i.e. split the data up by age
-- group and sex, and present these as fields in a different table, so we can
-- filter by them.

create or replace function sp_sex_workers_by_age_and_sex()
returns table (
    age_group text, 
    sex text, 
    value integer, 
    activity_report_form_id integer
) as $$
declare 
    row record;
begin
    drop table if exists temp_sex_workers;
    create temp table temp_sex_workers (
        age_group text,
        sex text, 
        value integer,
        activity_report_form_id integer
    );

    for row in
        select * from data_entry_sexworker
    loop
        insert into temp_sex_workers
            (age_group, sex, value, activity_report_form_id)
        values 
            ('10 to 14', 'Female', row.sex_workers_female_10_14, 
             row.activity_form_id),
            ('15 to 19', 'Female', row.sex_workers_female_15_19, 
             row.activity_form_id),
            ('20 to 24', 'Female', row.sex_workers_female_20_24, 
             row.activity_form_id),
            ('25 to 29', 'Female', row.sex_workers_female_25_29, 
             row.activity_form_id),
            ('30 to 34', 'Female', row.sex_workers_female_30_34, 
             row.activity_form_id),
            ('35 plus', 'Female', row.sex_workers_female_35_plus, 
             row.activity_form_id),
            ('10 to 14', 'Male', row.sex_workers_male_10_14, 
             row.activity_form_id),
            ('15 to 19', 'Male', row.sex_workers_male_15_19, 
             row.activity_form_id),
            ('20 to 24', 'Male', row.sex_workers_male_20_24, 
             row.activity_form_id),
            ('25 to 29', 'Male', row.sex_workers_male_25_29, 
             row.activity_form_id),
            ('30 to 34', 'Male', row.sex_workers_male_30_34, 
             row.activity_form_id),
            ('35 plus', 'Male', row.sex_workers_male_35_plus, 
             row.activity_form_id);
    end loop;

    return query
        select * from temp_sex_workers;
end;
$$ language plpgsql;

create or replace view vw_sex_workers_by_age_and_sex as
select ac.*, vw.*
from sp_sex_workers_by_age_and_sex() vw
left join vw_activityreportform ac
  on ac.id = vw.activity_report_form_id
  order by age_group;

create or replace function sp_out_of_school_by_age_and_sex()
returns table (
    age_group text, 
    sex text, 
    value integer, 
    activity_report_form_id integer
) as $$
declare 
    row record;
begin
    drop table if exists temp_outofschool;
    create temp table temp_outofschool (
        age_group text,
        sex text, 
        value integer,
        activity_report_form_id integer
    );

    for row in
        select * from data_entry_outofschool
    loop
        insert into temp_outofschool
            (age_group, sex, value, activity_report_form_id)
        values 
            ('10 to 14', 'Female', row.out_school_female_10_14, 
             row.activity_form_id),
            ('15 to 19', 'Female', row.out_school_female_15_19, 
             row.activity_form_id),
            ('20 to 24', 'Female', row.out_school_female_20_24, 
             row.activity_form_id),
            ('10 to 14', 'Male', row.out_school_male_10_14, 
             row.activity_form_id),
            ('15 to 19', 'Male', row.out_school_male_15_19, 
             row.activity_form_id),
            ('20 to 24', 'Male', row.out_school_male_20_24, 
             row.activity_form_id);
    end loop;

    return query
        select * from temp_outofschool;
end;
$$ language plpgsql;

/*drop view if exists vw_out_of_school_by_age_and_sex;*/ 
create or replace view vw_out_of_school_by_age_and_sex as
select ac.*, vw.*
from sp_out_of_school_by_age_and_sex() vw
left join vw_activityreportform ac
  on ac.id = vw.activity_report_form_id
  Order by age_group;

create or replace function sp_inmates_by_age_and_sex()
returns table (
    age_group text, 
    sex text, 
    value integer, 
    activity_report_form_id integer
) as $$
declare 
    row record;
begin
    drop table if exists temp_inmate;
    create temp table temp_inmate (
        age_group text,
        sex text, 
        value integer,
        activity_report_form_id integer
    );

    for row in
        select * from data_entry_inmate
    loop
        insert into temp_inmate
            (age_group, sex, value, activity_report_form_id)
        values 
            ('10 to 14', 'Female', row.inmate_female_10_14, 
             row.activity_form_id),
            ('15 to 19', 'Female', row.inmate_female_15_19, 
             row.activity_form_id),
            ('20 to 24', 'Female', row.inmate_female_20_24, 
             row.activity_form_id),
            ('10 to 14', 'Male', row.inmate_male_10_14, 
             row.activity_form_id),
            ('15 to 19', 'Male', row.inmate_male_15_19, 
             row.activity_form_id),
            ('20 to 24', 'Male', row.inmate_male_20_24, 
             row.activity_form_id);
    end loop;

    return query
        select * from temp_inmate;
end;
$$ language plpgsql;

create or replace view vw_inmate_by_age_and_sex as
select ac.*, vw.*
from sp_inmate_by_age_and_sex() vw
left join vw_activityreportform ac
  on ac.id = vw.activity_report_form_id
  Order by age_group;

create or replace function sp_reported_case_by_age_and_sex()
returns table (
    age_group text, 
    sex text, 
    value integer, 
    activity_report_form_id integer
) as $$
declare 
    row record;
begin
    drop table if exists temp_reportedcase;
    create temp table temp_reportedcase (
        age_group text,
        sex text, 
        value integer,
        activity_report_form_id integer
    );

    for row in
        select * from data_entry_reportedcase
    loop
        insert into temp_reportedcase
            (age_group, sex, value, activity_report_form_id)
        values 
            ('9 and less', 'Female', row.reported_female_less_10, 
             row.activity_form_id),
            ('10 to 14', 'Female', row.reported_female_10_14, 
             row.activity_form_id),
            ('15 to 19', 'Female', row.reported_female_15_19, 
             row.activity_form_id),
            ('20 to 24', 'Female', row.reported_female_20_24, 
             row.activity_form_id),
            ('25 plus', 'Female', row.reported_female_25_plus, 
             row.activity_form_id),
            ('9 and less', 'Male', row.reported_male_less_10, 
             row.activity_form_id),
            ('10 to 14', 'Male', row.reported_male_10_14, 
             row.activity_form_id),
            ('15 to 19', 'Male', row.reported_male_15_19, 
             row.activity_form_id),
            ('20 to 24', 'Male', row.reported_male_20_24, 
             row.activity_form_id),
            ('25 plus', 'Male', row.reported_male_25_plus, 
             row.activity_form_id);
    end loop;

    return query
        select * from temp_reportedcase;
end;
$$ language plpgsql;

create or replace view vw_reported_case_by_age_and_sex as
select ac.*, vw.*
from sp_reported_case_by_age_and_sex() vw
left outer join vw_activityreportform ac
  on ac.id = vw.activity_report_form_id
  order by age_group;

create or replace function sp_experienced_physical_violence_by_age_and_sex()
returns table (
    age_group text, 
    sex text, 
    value integer, 
    activity_report_form_id integer
) as $$
declare 
    row record;
begin
    drop table if exists temp_experiencedphysicalviolence;
    create temp table temp_experiencedphysicalviolence (
        age_group text,
        sex text, 
        value integer,
        activity_report_form_id integer
    );

    for row in
        select * from data_entry_experiencedphysicalviolence
    loop
        insert into temp_experiencedphysicalviolence
            (age_group, sex, value, activity_report_form_id)
        values 
            ('9 and less', 'Female', row.physical_female_less_10, 
             row.activity_form_id),
            ('10 to 14', 'Female', row.physical_female_10_14, 
             row.activity_form_id),
            ('15 to 19', 'Female', row.physical_female_15_19, 
             row.activity_form_id),
            ('20 to 24', 'Female', row.physical_female_20_24, 
             row.activity_form_id),
            ('25 plus', 'Female', row.physical_female_25_plus, 
             row.activity_form_id),
            ('9 and less', 'Male', row.physical_male_less_10, 
             row.activity_form_id),
            ('10 to 14', 'Male', row.physical_male_10_14, 
             row.activity_form_id),
            ('15 to 19', 'Male', row.physical_male_15_19, 
             row.activity_form_id),
            ('20 to 24', 'Male', row.physical_male_20_24, 
             row.activity_form_id),
            ('25 plus', 'Male', row.physical_male_25_plus, 
             row.activity_form_id);
    end loop;

    return query
        select * from temp_experiencedphysicalviolence;
end;
$$ language plpgsql;

create or replace view vw_experienced_physical_violence_by_age_and_sex as
select ac.*, vw.*
from sp_experienced_physical_violence_by_age_and_sex() vw
left outer join vw_activityreportform ac
  on ac.id = vw.activity_report_form_id
  order BY age_group;

create or replace function sp_experienced_sexual_violence_by_age_and_sex()
returns table (
    age_group text, 
    sex text, 
    value integer, 
    activity_report_form_id integer
) as $$
declare 
    row record;
begin
    drop table if exists temp_experiencedsexualviolence;
    create temp table temp_experiencedsexualviolence (
        age_group text,
        sex text, 
        value integer,
        activity_report_form_id integer
    );

    for row in
        select * from data_entry_experiencedsexualviolence
    loop
        insert into temp_experiencedsexualviolence
            (age_group, sex, value, activity_report_form_id)
        values 
            ('9 and less', 'Female', row.sexual_female_less_10, 
             row.activity_form_id),
            ('10 to 14', 'Female', row.sexual_female_10_14, 
             row.activity_form_id),
            ('15 to 19', 'Female', row.sexual_female_15_19, 
             row.activity_form_id),
            ('20 to 24', 'Female', row.sexual_female_20_24, 
             row.activity_form_id),
            ('25 plus', 'Female', row.sexual_female_25_plus, 
             row.activity_form_id),
            ('9 and less', 'Male', row.sexual_male_less_10, 
             row.activity_form_id),
            ('10 to 14', 'Male', row.sexual_male_10_14, 
             row.activity_form_id),
            ('15 to 19', 'Male', row.sexual_male_15_19, 
             row.activity_form_id),
            ('20 to 24', 'Male', row.sexual_male_20_24, 
             row.activity_form_id),
            ('25 plus', 'Male', row.sexual_male_25_plus, 
             row.activity_form_id);
    end loop;

    return query
        select * from temp_experiencedsexualviolence;
end;
$$ language plpgsql;

create or replace view vw_experienced_sexual_violence_by_age_and_sex as
select ac.*, vw.* 
from sp_experienced_sexual_violence_by_age_and_sex() vw
left outer join vw_activityreportform ac
  on ac.id = vw.activity_report_form_id
  order by age_group;

create or replace function sp_post_exposure_prophylaxis_by_age_and_sex()
returns table (
    age_group text, 
    sex text, 
    value integer, 
    activity_report_form_id integer
) as $$
declare 
    row record;
begin
    drop table if exists temp_postexposureprophylaxis;
    create temp table temp_postexposureprophylaxis (
        age_group text,
        sex text, 
        value integer,
        activity_report_form_id integer
    );

    for row in
        select * from data_entry_postexposureprophylaxis
    loop
        insert into temp_postexposureprophylaxis
            (age_group, sex, value, activity_report_form_id)
        values 
            ('9 and less', 'Female', row.accessed_pep_female_less_10, 
             row.activity_form_id),
            ('10 to 14', 'Female', row.accessed_pep_female_10_14, 
             row.activity_form_id),
            ('15 to 19', 'Female', row.accessed_pep_female_15_19, 
             row.activity_form_id),
            ('20 to 24', 'Female', row.accessed_pep_female_20_24, 
             row.activity_form_id),
            ('25 plus', 'Female', row.accessed_pep_female_25_plus, 
             row.activity_form_id),
            ('9 and less', 'Male', row.accessed_pep_male_less_10, 
             row.activity_form_id),
            ('10 to 14', 'Male', row.accessed_pep_male_10_14, 
             row.activity_form_id),
            ('15 to 19', 'Male', row.accessed_pep_male_15_19, 
             row.activity_form_id),
            ('20 to 24', 'Male', row.accessed_pep_male_20_24, 
             row.activity_form_id),
            ('25 plus', 'Male', row.accessed_pep_male_25_plus, 
             row.activity_form_id);
    end loop;

    return query
        select * from temp_postexposureprophylaxis;
end;
$$ language plpgsql;

create or replace view vw_post_exposure_prophylaxis_by_age_and_sex as
select ac.*, vw.* 
from sp_post_exposure_prophylaxis_by_age_and_sex() vw
left outer join vw_activityreportform ac
  on ac.id = vw.activity_report_form_id
  order by age_group;

create or replace function sp_individual_currently_enrolled_by_age_and_sex()
returns table (
    age_group text, 
    sex text, 
    value integer, 
    activity_report_form_id integer
) as $$
declare 
    row record;
begin
    drop table if exists temp_individualcurrentlyenrolled;
    create temp table temp_individualcurrentlyenrolled (
        age_group text,
        sex text, 
        value integer,
        activity_report_form_id integer
    );

    for row in
        select * from data_entry_individualcurrentlyenrolled
    loop
        insert into temp_individualcurrentlyenrolled
            (age_group, sex, value, activity_report_form_id)
        values 
            ('9 and less', 'Female', row.individuals_enrolled_female_10_less,
            	row.activity_form_id),

            ('10 to 14', 'Female', row.individuals_enrolled_female_10_14, 
             row.activity_form_id),
            ('15 to 19', 'Female', row.individuals_enrolled_female_15_19, 
             row.activity_form_id),
            ('20 to 24', 'Female', row.individuals_enrolled_female_20_24, 
             row.activity_form_id),
            ('25 and above', 'Female', row.individuals_enrolled_female_25_plus, 
             row.activity_form_id),
            ('9 and less', 'Male', row.individuals_enrolled_female_10_less,
            	row.activity_form_id),

            ('10 to 14', 'Male', row.individuals_enrolled_male_10_14, 
             row.activity_form_id),
            ('15 to 19', 'Male', row.individuals_enrolled_male_15_19, 
             row.activity_form_id),
            ('20 to 24', 'Male', row.individuals_enrolled_male_20_24, 
             row.activity_form_id),
            ('25 and above', 'Male', row.individuals_enrolled_male_25_plus, 
             row.activity_form_id);
    end loop;

    return query
        select * from temp_individualcurrentlyenrolled;
end;
$$ language plpgsql;

create or replace view vw_individual_currently_enrolled_by_age_and_sex as
select ac.*, vw.*
from sp_individual_currently_enrolled_by_age_and_sex() vw
left outer join vw_activityreportform ac
  on ac.id = vw.activity_report_form_id
  order by age_group;

create or replace function sp_vulnerable_people_by_age_and_sex()
returns table (
    age_group text, 
    sex text, 
    value integer, 
    activity_report_form_id integer
) as $$
declare 
    row record;
begin
    drop table if exists temp_vulnerablepeople;
    create temp table temp_vulnerablepeople (
        age_group text,
        sex text, 
        value integer,
        activity_report_form_id integer
    );

    for row in
        select * from data_entry_vulnerablepeople
    loop
        insert into temp_vulnerablepeople
            (age_group, sex, value, activity_report_form_id)
        values 
            ('9 and less', 'Female', row.ovc_female_less_10, 
             row.activity_form_id),
            ('10 to 14', 'Female', row.ovc_female_10_14, 
             row.activity_form_id),
            ('15 to 19', 'Female', row.ovc_female_15_19, 
               row.activity_form_id),
            ('20 to 24', 'Female', row.ovc_female_20_24, 
             row.activity_form_id),
            ('25 plus', 'Female', row.ovc_female_25_plus, 
             row.activity_form_id),
            ('9 and less', 'Male', row.ovc_male_less_10, 
             row.activity_form_id),
            ('10 to 14', 'Male', row.ovc_male_10_14, 
             row.activity_form_id),
            ('15 to 19', 'Male', row.ovc_male_15_19, 
             row.activity_form_id),
            ('20 to 24', 'Male', row.ovc_male_20_24, 
             row.activity_form_id),
            ('25 plus', 'Male', row.ovc_male_25_plus, 
             row.activity_form_id);
    end loop;

    return query
        select * from temp_vulnerablepeople;
end;
$$ language plpgsql;

create or replace view vw_vulnerable_people_by_age_and_sex as
select ac.*, vw.* 
from sp_vulnerable_people_by_age_and_sex() vw
left outer join vw_activityreportform ac
  on ac.id = vw.activity_report_form_id
  order by age_group;

create or replace function sp_pre_exposure_prophylaxis_by_age_and_sex()
returns table (
    age_group text, 
    sex text, 
    value integer, 
    activity_report_form_id integer
) as $$
declare 
    row record;
begin
    drop table if exists temp_preexposureprophylaxis;
    create temp table temp_preexposureprophylaxis (
        age_group text,
        sex text, 
        value integer,
        activity_report_form_id integer
    );

    for row in
        select * from data_entry_preexposureprophylaxis
    loop
        insert into temp_preexposureprophylaxis
            (age_group, sex, value, activity_report_form_id)
        values 
            ('15 to 19', 'Female', row.referred_pep_female_15_19, 
             row.activity_form_id),
            ('20 to 24', 'Female', row.referred_pep_female_20_24, 
             row.activity_form_id),
            ('25 plus', 'Female', row.referred_pep_female_25_plus, 
             row.activity_form_id),
            ('15 to 19', 'Male', row.referred_pep_male_15_19, 
             row.activity_form_id),
            ('20 to 24', 'Male', row.referred_pep_male_20_24, 
             row.activity_form_id),
            ('25 plus', 'Male', row.referred_pep_male_25_plus, 
             row.activity_form_id);
    end loop;

    return query
        select * from temp_preexposureprophylaxis;
end;
$$ language plpgsql;

create or replace view vw_pre_exposure_prophylaxis_by_age_and_sex as
select ac.*, vw.* 
from sp_pre_exposure_prophylaxis_by_age_and_sex() vw
left outer join vw_activityreportform ac
  on ac.id = vw.activity_report_form_id
  order by age_group;

CREATE OR REPLACE VIEW vw_keypop_export AS
SELECT vw_activityreportform.id,
       organisation,
       organisation_address AS "organisation_address",
       start_year AS "start_year",
       gps AS "gps",
       website AS "website",
       description_of_organisation AS "description_of_organisation",
       key_contact_name AS "key_contact_name",
       position_within_organisation AS "position_within_organisation",
       telephone_number AS "telephone_number",
       telephone_number_alternative AS "telephone_number_alternative",
       email_address AS "email_address", 
       permanent_employee_female AS "permanent_employee_female",
       permanent_employee_male AS "permanent_employee_male",
       temporary_employee_female AS "temporary_employee_female",
       temporary_employee_male AS "temporary_employee_male",
       volunteer_employee_female AS "volunteer_employee_female",
       volunteer_employee_male AS "volunteer_employee_male",
       organisation_type AS "organisation_type",
       national_organisation_id AS "national_organisation_id",
       organisation_province_id AS "organisation_province_id",
       organisation_district_id AS "organisation_district_id",
       province_name AS "province_name",
       district_name AS "district_name",
       activityreportform_report_date,
       activityreportform_quarter_been_reported,
       activityreportform_name,
       activityreportform_telephone_number,
       activityreportform_email_address,
       activityreportform_id,
       
       data_entry_inmate.inmates_female_num,
       data_entry_inmate.inmates_male_num,
       data_entry_sexworker.sex_workers_male_10_14 AS "Sex_worker_Male_10_14",
       data_entry_sexworker.sex_workers_male_15_19 AS "Sex_worker_Male_15_19",
       data_entry_sexworker.sex_workers_male_20_24 AS "Sex_worker_Male_20_24",
       data_entry_sexworker.sex_workers_male_25_29 AS "Sex_worker_Male_25_29",
       data_entry_sexworker.sex_workers_male_30_34 AS "Sex_worker_Male_30_34",
       data_entry_sexworker.sex_workers_male_35_plus AS "Sex_worker_Male_35_plus",
       data_entry_sexworker.sex_workers_female_10_14 AS "Sex_worker_Female_10_14",
       data_entry_sexworker.sex_workers_female_15_19 AS "Sex_worker_Female_15_19",
       data_entry_sexworker.sex_workers_female_20_24 AS "Sex_worker_Female_20_24",
       data_entry_sexworker.sex_workers_female_25_29 AS "Sex_worker_Female_25_29",
       data_entry_sexworker.sex_workers_female_30_34 AS "Sex_worker_Female_30_34",
       data_entry_sexworker.sex_workers_female_35_plus AS "Sex_worker_Female_35_plus",
       data_entry_inmate.inmates_female_num AS "Inmate_Female_Number",
       data_entry_inmate.inmates_male_num AS "Inmate_Male_Number",
       data_entry_personswithdisabilty.pwd_female_num AS "PWD_Female_Number",
       data_entry_personswithdisabilty.pwd_male_num AS "PWD_Male_Number", 
       data_entry_mobileworker.mobile_workers_female_num AS "Mobile_Workers_Female_Number",
       data_entry_mobileworker.mobile_workers_male_num AS "Mobile_Workers_Male_Number",
       data_entry_mobilepopulation.other_mobile_population AS "Mobile_Population",
       data_entry_menwithmen.men_with_men AS "Men_with_Men",
       data_entry_transgenderindividual.transgender_num AS "Transgender_Number",
       data_entry_peoplewhoinjectdrug.pwid_male AS "PWID_Male",
       data_entry_peoplewhoinjectdrug.pwid_female AS "PWID_Female"
       FROM vw_activityreportform
       LEFT OUTER JOIN data_entry_supportfield ON vw_activityreportform.id = data_entry_supportfield.id
       LEFT OUTER JOIN data_entry_peoplewhoinjectdrug ON vw_activityreportform.id = data_entry_peoplewhoinjectdrug.activity_form_id
       LEFT OUTER JOIN data_entry_transgenderindividual ON vw_activityreportform.id = data_entry_transgenderindividual.activity_form_id
       LEFT OUTER JOIN data_entry_menwithmen ON vw_activityreportform.id = data_entry_menwithmen.activity_form_id
       LEFT OUTER JOIN data_entry_personswithdisabilty ON vw_activityreportform.id = data_entry_personswithdisabilty.activity_form_id
       LEFT OUTER JOIN data_entry_mobilepopulation ON vw_activityreportform.id = data_entry_mobilepopulation.id
       LEFT OUTER JOIN data_entry_mobileworker ON vw_activityreportform.id = data_entry_mobileworker.activity_form_id
       LEFT OUTER JOIN data_entry_sexworker ON vw_activityreportform.id = data_entry_sexworker.activity_form_id
       LEFT OUTER JOIN data_entry_inmate ON vw_activityreportform.id = data_entry_inmate.activity_form_id
       --GROUP BY organisaton.data_entry_iecmaterial

       CREATE OR REPLACE VIEW vw_sarf_export AS
SELECT vw_activityreportform.id,
       organisation,
       organisation_address AS "organisation_address",
       start_year AS "start_year",
       gps AS "gps",
       website AS "website",
       description_of_organisation AS "description_of_organisation",
       key_contact_name AS "key_contact_name",
       position_within_organisation AS "position_within_organisation",
       telephone_number AS "telephone_number",
       telephone_number_alternative AS "telephone_number_alternative",
       email_address AS "email_address", 
       permanent_employee_female AS "permanent_employee_female",
       permanent_employee_male AS "permanent_employee_male",
       temporary_employee_female AS "temporary_employee_female",
       temporary_employee_male AS "temporary_employee_male",
       volunteer_employee_female AS "volunteer_employee_female",
       volunteer_employee_male AS "volunteer_employee_male",
       organisation_type AS "organisation_type",
       national_organisation_id AS "national_organisation_id",
       organisation_province_id AS "organisation_province_id",
       organisation_district_id AS "organisation_district_id",
       province_name AS "province_name",
       district_name AS "district_name",
       activityreportform_report_date,
       activityreportform_quarter_been_reported,
       activityreportform_name,
       activityreportform_telephone_number,
       activityreportform_email_address,
       activityreportform_id,
       data_entry_iecmaterial.material_type AS "material_type",
       data_entry_iecmaterial.number_distributed AS "number_distributed",
       data_entry_iecmaterial.localized AS "localized",
       data_entry_iecmaterial2_target_audience.iecmaterial2_id,
       data_entry_iecmaterial2_target_audience.organisationtarget_id AS "Organisation_Target_ID",
       data_entry_iecmaterial2.other_target_audience AS "Other_Target_Audience",
       data_entry_inmate.inmates_female_num,
       data_entry_inmate.inmates_male_num,
       data_entry_teachers.teachers_female AS "female_teachers",
       data_entry_teachers.teachers_male AS "male_teachers",
       data_entry_outofschool.out_school_female_10_14 AS "Out_of_school_Female_10_14",
       data_entry_outofschool.out_school_female_15_19 AS "Out_of_school_Female_15_19",
       data_entry_outofschool.out_school_female_20_24 AS "Out_of_school_Female_20_24",
       data_entry_outofschool.out_school_male_10_14 AS "Out_of_school_Male_10_14",
       data_entry_outofschool.out_school_male_15_19 AS "Out_of_school_Male_15_19",
       data_entry_outofschool.out_school_male_20_24 AS "Out_of_school_Male_20_24",
       data_entry_sexworker.sex_workers_male_10_14 AS "Sex_worker_Male_10_14",
       data_entry_sexworker.sex_workers_male_15_19 AS "Sex_worker_Male_15_19",
       data_entry_sexworker.sex_workers_male_20_24 AS "Sex_worker_Male_20_24",
       data_entry_sexworker.sex_workers_male_25_29 AS "Sex_worker_Male_25_29",
       data_entry_sexworker.sex_workers_male_30_34 AS "Sex_worker_Male_30_34",
       data_entry_sexworker.sex_workers_male_35_plus AS "Sex_worker_Male_35_plus",
       data_entry_sexworker.sex_workers_female_10_14 AS "Sex_worker_Female_10_14",
       data_entry_sexworker.sex_workers_female_15_19 AS "Sex_worker_Female_15_19",
       data_entry_sexworker.sex_workers_female_20_24 AS "Sex_worker_Female_20_24",
       data_entry_sexworker.sex_workers_female_25_29 AS "Sex_worker_Female_25_29",
       data_entry_sexworker.sex_workers_female_30_34 AS "Sex_worker_Female_30_34",
       data_entry_sexworker.sex_workers_female_35_plus AS "Sex_worker_Female_35_plus",
       data_entry_personswithdisabilty.pwd_female_num AS "PWD_Female_Number",
       data_entry_personswithdisabilty.pwd_male_num AS "PWD_Male_Number", 
       data_entry_mobileworker.mobile_workers_female_num AS "Mobile_Workers_Female_Number",
       data_entry_mobileworker.mobile_workers_male_num AS "Mobile_Workers_Male_Number",
       --data_entry_mobilepopulationtype.mobile_population_type AS "Mobile_Population_Type",//RETURNING NO DATA
       data_entry_menwithmen.men_with_men AS "Men_with_Men",
       data_entry_transgenderindividual.transgender_num AS "Transgender_Number",
       data_entry_peoplewhoinjectdrug.pwid_male AS "PWID_Male",
       data_entry_peoplewhoinjectdrug.pwid_female AS "PWID_Female",
       data_entry_condomprogramming.condom_dist_point_num AS "Condom_Distribution_Point_Number",
       data_entry_condomprogramming2.female_condom_distributed_num AS "Female_Condom_Distributed_Number",
       data_entry_condomprogramming2.male_condom_distributed_num AS "Male_Condom_Distributed_Number",
       data_entry_experiencedphysicalviolence.physical_female_less_10 AS "Physical_Female_Less_10",
       data_entry_experiencedphysicalviolence.physical_female_10_14 AS "Physical_Female_10_14",
       data_entry_experiencedphysicalviolence.physical_female_15_19 AS "Physical_Female_15_19",
       data_entry_experiencedphysicalviolence.physical_female_20_24 AS "Physical_Female_20_24",
       data_entry_experiencedphysicalviolence.physical_female_25_plus AS "Physical_Female_25_plus",
       data_entry_experiencedphysicalviolence.physical_male_less_10 AS "Physical_Male_Less_10",
       data_entry_experiencedphysicalviolence.physical_male_10_14 AS "Physical_Male_10_14",
       data_entry_experiencedphysicalviolence.physical_male_15_19 AS "Physical_Male_15_19",
       data_entry_experiencedphysicalviolence.physical_male_20_24 AS "Physical_Male_20_24",
       data_entry_experiencedphysicalviolence.physical_male_25_plus AS "Physical_Male_25_plus",
       data_entry_experiencedsexualviolence.sexual_female_less_10 AS "Sexual_Female_Less_10",
       data_entry_experiencedSexualviolence.sexual_female_10_14 AS "Sexual_Female_10_14",
       data_entry_experiencedSexualviolence.Sexual_female_15_19 AS "Sexua_Female_15_19",
       data_entry_experiencedSexualviolence.Sexual_female_20_24 AS "Sexual_Female_20_24",
       data_entry_experiencedSexualviolence.Sexual_female_25_plus AS "Sexual_Female_25_plus",
       data_entry_experiencedSexualviolence.Sexual_male_less_10 AS "Sexual_Male_Less_10",
       data_entry_experiencedSexualviolence.Sexual_male_10_14 AS "Sexual_Male_10_14",
       data_entry_experiencedSexualviolence.Sexual_male_15_19 AS "Sexual_Male_15_19",
       data_entry_experiencedSexualviolence.Sexual_male_20_24 AS "Sexual_Male_20_24",
       data_entry_experiencedSexualviolence.Sexual_male_25_plus AS "Sexual_Male_25_plus",
       data_entry_postexposureprophylaxis.accessed_pep_male_less_10 AS "Accessed_PEP_Male_less_10",
       data_entry_postexposureprophylaxis.accessed_pep_male_10_14 AS "Accessed_PEP_Male_10_14",
       data_entry_postexposureprophylaxis.accessed_pep_male_15_19 AS "Accessed_PEP_Male_15_19",
       data_entry_postexposureprophylaxis.accessed_pep_male_20_24 AS "Accessed_PEP_Male_20_24",
       data_entry_postexposureprophylaxis.accessed_pep_male_25_plus AS "Accessed_PEP_Male_25_plus",
        data_entry_postexposureprophylaxis.accessed_pep_female_less_10 AS "Accessed_PEP_Female_less_10",
       data_entry_postexposureprophylaxis.accessed_pep_female_10_14 AS "Aceessed_PEP_Femal_10_14",
       data_entry_postexposureprophylaxis.accessed_pep_female_15_19 AS "Accessed_PEP_Female_15_19",
       data_entry_postexposureprophylaxis.accessed_pep_female_20_24 AS "Accessed_PEP_Female_20_24",
       data_entry_postexposureprophylaxis.accessed_pep_female_25_plus AS "Accessed_PEP_Female_25_plus",
       data_entry_preexposureprophylaxis.referred_pep_male_15_19 AS "Referred_PEP_Male_15_19",
       data_entry_preexposureprophylaxis.referred_pep_male_20_24 AS "Referred_PEP_Male_20_24",
       data_entry_preexposureprophylaxis.referred_pep_male_25_plus AS "Referred_PEP_Male_25_plus",
       data_entry_preexposureprophylaxis.referred_pep_female_15_19 AS "Referred_PEP_Female_15_19",
       data_entry_preexposureprophylaxis.referred_pep_female_20_24 AS "Referred_PEP_Female_20_24",
       data_entry_preexposureprophylaxis.referred_pep_female_25_plus AS "Referred_PEP_Female_25_plus",
       data_entry_supportgroupsetup.support_groups AS "Support_Groups",
       data_entry_individualcurrentlyenrolled.individuals_enrolled_male_10_14 AS "Individuals_Enrolled_Male_10_14",
       data_entry_individualcurrentlyenrolled.individuals_enrolled_male_15_19 AS "Individuals_Enrolled_Male_15_19",
       data_entry_individualcurrentlyenrolled.individuals_enrolled_male_20_24 AS "Individuals_Enrolled_Male_20_24",
       data_entry_individualcurrentlyenrolled.individuals_enrolled_male_25_plus AS "Individuals_Enroled_Male_25",
        data_entry_individualcurrentlyenrolled.individuals_enrolled_female_10_14 AS "Individuals_Enrolled_Female_10_14",
       data_entry_individualcurrentlyenrolled.individuals_enrolled_female_15_19 AS "Individuals_Enrolled_Female_15_19",
       data_entry_individualcurrentlyenrolled.individuals_enrolled_female_20_24 AS "Individuals_Enrolled_Female_20_24",
       data_entry_individualcurrentlyenrolled.individuals_enrolled_female_25_plus AS "Individuals_Enroled_Female_25",
       data_entry_vulnerablepeople.ovc_male_less_10 AS "OVC_Male_Less_10",
       data_entry_vulnerablepeople.ovc_male_10_14 AS "OVC_Male_10_14",
       data_entry_vulnerablepeople.ovc_male_15_19 AS "OVC_Male_15_19",
       data_entry_vulnerablepeople.ovc_male_20_24 AS "OVC_Male_20_24",
       data_entry_vulnerablepeople.ovc_male_25_plus AS "OVC_Male_25_plus",
       data_entry_vulnerablepeople.ovc_female_less_10 AS "OVC_Female_Less_10",
       data_entry_vulnerablepeople.ovc_female_10_14 AS "OVC_Female_10_14",
       data_entry_vulnerablepeople.ovc_female_15_19 AS "OVC_Female_15_19",
       data_entry_vulnerablepeople.ovc_female_20_24 AS "OVC_Female_20_24",
       data_entry_vulnerablepeople.ovc_female_25_plus AS "OVC_Female_25_plus",
       data_entry_stakeholderverification.acknowledgement AS "Stakeholder_Acknowledgement",
       data_entry_stakeholderverification.stakeholder_initials AS "Stakeholder_Initials", 
       data_entry_supportfield.area_of_support AS "Area_of_Support", 
      data_entry_dacavalidation.validation_date AS "DACA_Validation_Date",
      data_entry_dacavalidation.validated_by_id AS "DACA_Validated_By_ID",
      data_entry_dacavalidation.validation_status AS "DACA_Validation_Status",
      data_entry_dacavalidation.acknowledgement AS "DACA_Acknowledgement",
      data_entry_dacavalidation.daca_initials AS "DACA_Initials",
      data_entry_pitmeovalidation.validation_date AS "PITMEO_Validation_Date",
      data_entry_pitmeovalidation.validation_status AS "PITMEO_Validation_Status",
      data_entry_pitmeovalidation.acknowledgement AS "PITMEO_Acknowledgement"
       FROM vw_activityreportform
       LEFT OUTER JOIN data_entry_dacavalidation ON vw_activityreportform.id = data_entry_dacavalidation.activity_form_id
       LEFT OUTER JOIN data_entry_pitmeovalidation ON vw_activityreportform.id = data_entry_pitmeovalidation.activity_form_id
       LEFT OUTER JOIN data_entry_supportfield ON vw_activityreportform.id = data_entry_supportfield.id
       LEFT OUTER JOIN data_entry_stakeholderverification ON vw_activityreportform.id = data_entry_stakeholderverification.activity_form_id
       LEFT OUTER JOIN data_entry_vulnerablepeople ON vw_activityreportform.id = data_entry_vulnerablepeople.activity_form_id
       LEFT OUTER JOIN data_entry_individualcurrentlyenrolled ON vw_activityreportform.id = data_entry_individualcurrentlyenrolled.activity_form_id
       LEFT OUTER JOIN data_entry_supportgroupsetup ON vw_activityreportform.id = data_entry_supportgroupsetup.activity_form_id
       LEFT OUTER JOIN data_entry_preexposureprophylaxis ON vw_activityreportform.id = data_entry_preexposureprophylaxis.activity_form_id
       LEFT OUTER JOIN data_entry_postexposureprophylaxis ON vw_activityreportform.id = data_entry_postexposureprophylaxis.activity_form_id
       LEFT OUTER JOIN data_entry_experiencedphysicalviolence ON vw_activityreportform.id = data_entry_experiencedphysicalviolence.activity_form_id
       LEFT OUTER JOIN data_entry_experiencedsexualviolence ON vw_activityreportform.id = data_entry_experiencedsexualviolence.activity_form_id
       LEFT OUTER JOIN data_entry_condomprogramming2 ON vw_activityreportform.id = data_entry_condomprogramming2.activity_form_id
       LEFT OUTER JOIN data_entry_condomprogramming ON vw_activityreportform.id = data_entry_condomprogramming.activity_form_id
       LEFT OUTER JOIN data_entry_peoplewhoinjectdrug ON vw_activityreportform.id = data_entry_peoplewhoinjectdrug.activity_form_id
       LEFT OUTER JOIN data_entry_transgenderindividual ON vw_activityreportform.id = data_entry_transgenderindividual.activity_form_id
       LEFT OUTER JOIN data_entry_menwithmen ON vw_activityreportform.id = data_entry_menwithmen.activity_form_id
       LEFT OUTER JOIN data_entry_personswithdisabilty ON vw_activityreportform.id = data_entry_personswithdisabilty.activity_form_id
       LEFT OUTER JOIN data_entry_mobilepopulationtype ON vw_activityreportform.id = data_entry_mobilepopulationtype.id
       LEFT OUTER JOIN data_entry_mobileworker ON vw_activityreportform.id = data_entry_mobileworker.activity_form_id
LEFT OUTER JOIN data_entry_sexworker ON vw_activityreportform.id = data_entry_sexworker.activity_form_id
LEFT OUTER JOIN data_entry_outofschool ON vw_activityreportform.id = data_entry_outofschool.activity_form_id
LEFT OUTER JOIN data_entry_iecmaterial ON vw_activityreportform.id = data_entry_iecmaterial.activity_form_id
LEFT OUTER JOIN data_entry_iecmaterial2_target_audience ON vw_activityreportform.id = data_entry_iecmaterial2_target_audience.id
LEFT OUTER JOIN data_entry_iecmaterial2 ON vw_activityreportform.id = data_entry_iecmaterial2.activity_form_id
LEFT OUTER JOIN data_entry_inmate ON vw_activityreportform.id = data_entry_inmate.activity_form_id
LEFT OUTER JOIN data_entry_teachers ON vw_activityreportform.id = data_entry_teachers.activity_form_id
--GROUP BY organisaton.data_entry_iecmaterial

