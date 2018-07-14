-- Apply with: psql nacmis -f storedprocs.sql

-- pick apart the data_entry_sexworker table, i.e. split the data up by age
-- group and sex, and present these as fields in a different table, so we can
-- filter by them.
create or replace function sp_sex_workers_by_age_and_sex()
returns table (
    indicator_name text, 
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
        indicator_name text,
        age_group text,
        sex text, 
        value integer,
        activity_report_form_id integer
    );

    for row in
        select * from data_entry_sexworker
    loop
        insert into temp_sex_workers
            (indicator_name, age_group, sex, value, activity_report_form_id)
        values 
            ('sex_workers', '10_14', 'female', row.sex_workers_female_10_14, 
             row.activity_form_id),
            ('sex_workers', '15_19', 'female', row.sex_workers_female_15_19, 
             row.activity_form_id),
            ('sex_workers', '20_24', 'female', row.sex_workers_female_20_24, 
             row.activity_form_id),
            ('sex_workers', '25_29', 'female', row.sex_workers_female_25_29, 
             row.activity_form_id),
            ('sex_workers', '30_34', 'female', row.sex_workers_female_30_34, 
             row.activity_form_id),
            ('sex_workers', '35_plus', 'female', row.sex_workers_female_35_plus, 
             row.activity_form_id),
            ('sex_workers', '10_14', 'male', row.sex_workers_male_10_14, 
             row.activity_form_id),
            ('sex_workers', '15_19', 'male', row.sex_workers_male_15_19, 
             row.activity_form_id),
            ('sex_workers', '20_24', 'male', row.sex_workers_male_20_24, 
             row.activity_form_id),
            ('sex_workers', '25_29', 'male', row.sex_workers_male_25_29, 
             row.activity_form_id),
            ('sex_workers', '30_34', 'male', row.sex_workers_male_30_34, 
             row.activity_form_id),
            ('sex_workers', '35_plus', 'male', row.sex_workers_male_35_plus, 
             row.activity_form_id);
    end loop;

    return query
        select * from temp_sex_workers;
end;
$$ language plpgsql;

create or replace function sp_out_of_school_by_age_and_sex()
returns table (
    indicator_name text, 
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
        indicator_name text,
        age_group text,
        sex text, 
        value integer,
        activity_report_form_id integer
    );

    for row in
        select * from data_entry_outofschool
    loop
        insert into temp_outofschool
            (indicator_name, age_group, sex, value, activity_report_form_id)
        values 
            ('out_school', '10_14', 'female', row.out_school_female_10_14, 
             row.activity_form_id),
            ('out_school', '15_19', 'female', row.out_school_female_15_19, 
             row.activity_form_id),
            ('out_school', '20_24', 'female', row.out_school_female_20_24, 
             row.activity_form_id),
            ('out_school', '10_14', 'male', row.out_school_male_10_14, 
             row.activity_form_id),
            ('out_school', '15_19', 'male', row.out_school_male_15_19, 
             row.activity_form_id),
            ('out_school', '20_24', 'male', row.out_school_male_20_24, 
             row.activity_form_id);
    end loop;

    return query
        select * from temp_outofschool;
end;
$$ language plpgsql;

create or replace function sp_reported_case_by_age_and_sex()
returns table (
    indicator_name text, 
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
        indicator_name text,
        age_group text,
        sex text, 
        value integer,
        activity_report_form_id integer
    );

    for row in
        select * from data_entry_reportedcase
    loop
        insert into temp_reportedcase
            (indicator_name, age_group, sex, value, activity_report_form_id)
        values 
            ('reported', 'less_10', 'female', row.reported_female_less_10, 
             row.activity_form_id),
            ('reported', '10_14', 'female', row.reported_female_10_14, 
             row.activity_form_id),
            ('reported', '15_19', 'female', row.reported_female_15_19, 
             row.activity_form_id),
            ('reported', '20_24', 'female', row.reported_female_20_24, 
             row.activity_form_id),
            ('reported', '25_plus', 'female', row.reported_female_25_plus, 
             row.activity_form_id),
            ('reported', 'less_10', 'male', row.reported_male_less_10, 
             row.activity_form_id),
            ('reported', '10_14', 'male', row.reported_male_10_14, 
             row.activity_form_id),
            ('reported', '15_19', 'male', row.reported_male_15_19, 
             row.activity_form_id),
            ('reported', '20_24', 'male', row.reported_male_20_24, 
             row.activity_form_id),
            ('reported', '25_plus', 'male', row.reported_male_25_plus, 
             row.activity_form_id);
    end loop;

    return query
        select * from temp_reportedcase;
end;
$$ language plpgsql;

create or replace function sp_experienced_physical_violence_by_age_and_sex()
returns table (
    indicator_name text, 
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
        indicator_name text,
        age_group text,
        sex text, 
        value integer,
        activity_report_form_id integer
    );

    for row in
        select * from data_entry_experiencedphysicalviolence
    loop
        insert into temp_experiencedphysicalviolence
            (indicator_name, age_group, sex, value, activity_report_form_id)
        values 
            ('physical', 'less_10', 'female', row.physical_female_less_10, 
             row.activity_form_id),
            ('physical', '10_14', 'female', row.physical_female_10_14, 
             row.activity_form_id),
            ('physical', '15_19', 'female', row.physical_female_15_19, 
             row.activity_form_id),
            ('physical', '20_24', 'female', row.physical_female_20_24, 
             row.activity_form_id),
            ('physical', '25_plus', 'female', row.physical_female_25_plus, 
             row.activity_form_id),
            ('physical', 'less_10', 'male', row.physical_male_less_10, 
             row.activity_form_id),
            ('physical', '10_14', 'male', row.physical_male_10_14, 
             row.activity_form_id),
            ('physical', '15_19', 'male', row.physical_male_15_19, 
             row.activity_form_id),
            ('physical', '20_24', 'male', row.physical_male_20_24, 
             row.activity_form_id),
            ('physical', '25_plus', 'male', row.physical_male_25_plus, 
             row.activity_form_id);
    end loop;

    return query
        select * from temp_experiencedphysicalviolence;
end;
$$ language plpgsql;

create or replace function sp_experienced_sexual_violence_by_age_and_sex()
returns table (
    indicator_name text, 
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
        indicator_name text,
        age_group text,
        sex text, 
        value integer,
        activity_report_form_id integer
    );

    for row in
        select * from data_entry_experiencedsexualviolence
    loop
        insert into temp_experiencedsexualviolence
            (indicator_name, age_group, sex, value, activity_report_form_id)
        values 
            ('sexual', 'less_10', 'female', row.sexual_female_less_10, 
             row.activity_form_id),
            ('sexual', '10_14', 'female', row.sexual_female_10_14, 
             row.activity_form_id),
            ('sexual', '15_19', 'female', row.sexual_female_15_19, 
             row.activity_form_id),
            ('sexual', '20_24', 'female', row.sexual_female_20_24, 
             row.activity_form_id),
            ('sexual', '25_plus', 'female', row.sexual_female_25_plus, 
             row.activity_form_id),
            ('sexual', 'less_10', 'male', row.sexual_male_less_10, 
             row.activity_form_id),
            ('sexual', '10_14', 'male', row.sexual_male_10_14, 
             row.activity_form_id),
            ('sexual', '15_19', 'male', row.sexual_male_15_19, 
             row.activity_form_id),
            ('sexual', '20_24', 'male', row.sexual_male_20_24, 
             row.activity_form_id),
            ('sexual', '25_plus', 'male', row.sexual_male_25_plus, 
             row.activity_form_id);
    end loop;

    return query
        select * from temp_experiencedsexualviolence;
end;
$$ language plpgsql;

create or replace function sp_post_exposure_prophylaxis_by_age_and_sex()
returns table (
    indicator_name text, 
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
        indicator_name text,
        age_group text,
        sex text, 
        value integer,
        activity_report_form_id integer
    );

    for row in
        select * from data_entry_postexposureprophylaxis
    loop
        insert into temp_postexposureprophylaxis
            (indicator_name, age_group, sex, value, activity_report_form_id)
        values 
            ('accessed_pep', 'less_10', 'female', row.accessed_pep_female_less_10, 
             row.activity_form_id),
            ('accessed_pep', '10_14', 'female', row.accessed_pep_female_10_14, 
             row.activity_form_id),
            ('accessed_pep', '15_19', 'female', row.accessed_pep_female_15_19, 
             row.activity_form_id),
            ('accessed_pep', '20_24', 'female', row.accessed_pep_female_20_24, 
             row.activity_form_id),
            ('accessed_pep', '25_plus', 'female', row.accessed_pep_female_25_plus, 
             row.activity_form_id),
            ('accessed_pep', 'less_10', 'male', row.accessed_pep_male_less_10, 
             row.activity_form_id),
            ('accessed_pep', '10_14', 'male', row.accessed_pep_male_10_14, 
             row.activity_form_id),
            ('accessed_pep', '15_19', 'male', row.accessed_pep_male_15_19, 
             row.activity_form_id),
            ('accessed_pep', '20_24', 'male', row.accessed_pep_male_20_24, 
             row.activity_form_id),
            ('accessed_pep', '25_plus', 'male', row.accessed_pep_male_25_plus, 
             row.activity_form_id);
    end loop;

    return query
        select * from temp_postexposureprophylaxis;
end;
$$ language plpgsql;

create or replace function sp_individual_currently_enrolled_by_age_and_sex()
returns table (
    indicator_name text, 
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
        indicator_name text,
        age_group text,
        sex text, 
        value integer,
        activity_report_form_id integer
    );

    for row in
        select * from data_entry_individualcurrentlyenrolled
    loop
        insert into temp_individualcurrentlyenrolled
            (indicator_name, age_group, sex, value, activity_report_form_id)
        values 
            ('individuals_enrolled', '10_14', 'female', row.individuals_enrolled_female_10_14, 
             row.activity_form_id),
            ('individuals_enrolled', '15_19', 'female', row.individuals_enrolled_female_15_19, 
             row.activity_form_id),
            ('individuals_enrolled', '20_24', 'female', row.individuals_enrolled_female_20_24, 
             row.activity_form_id),
            ('individuals_enrolled', '25_plus', 'female', row.individuals_enrolled_female_25_plus, 
             row.activity_form_id),
            ('individuals_enrolled', '10_14', 'male', row.individuals_enrolled_male_10_14, 
             row.activity_form_id),
            ('individuals_enrolled', '15_19', 'male', row.individuals_enrolled_male_15_19, 
             row.activity_form_id),
            ('individuals_enrolled', '20_24', 'male', row.individuals_enrolled_male_20_24, 
             row.activity_form_id),
            ('individuals_enrolled', '25_plus', 'male', row.individuals_enrolled_male_25_plus, 
             row.activity_form_id);
    end loop;

    return query
        select * from temp_individualcurrentlyenrolled;
end;
$$ language plpgsql;

create or replace function sp_vulnerable_people_by_age_and_sex()
returns table (
    indicator_name text, 
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
        indicator_name text,
        age_group text,
        sex text, 
        value integer,
        activity_report_form_id integer
    );

    for row in
        select * from data_entry_vulnerablepeople
    loop
        insert into temp_vulnerablepeople
            (indicator_name, age_group, sex, value, activity_report_form_id)
        values 
            ('ovc', 'less_10', 'female', row.ovc_female_less_10, 
             row.activity_form_id),
            ('ovc', '10_14', 'female', row.ovc_female_10_14, 
             row.activity_form_id),
            ('ovc', '15_19', 'female', row.ovc_female_15_19, 
             row.activity_form_id),
            ('ovc', '20_24', 'female', row.ovc_female_20_24, 
             row.activity_form_id),
            ('ovc', '25_plus', 'female', row.ovc_female_25_plus, 
             row.activity_form_id),
            ('ovc', 'less_10', 'male', row.ovc_male_less_10, 
             row.activity_form_id),
            ('ovc', '10_14', 'male', row.ovc_male_10_14, 
             row.activity_form_id),
            ('ovc', '15_19', 'male', row.ovc_male_15_19, 
             row.activity_form_id),
            ('ovc', '20_24', 'male', row.ovc_male_20_24, 
             row.activity_form_id),
            ('ovc', '25_plus', 'male', row.ovc_male_25_plus, 
             row.activity_form_id);
    end loop;

    return query
        select * from temp_vulnerablepeople;
end;
$$ language plpgsql;

create or replace function sp_pre_exposure_prophylaxis_by_age_and_sex()
returns table (
    indicator_name text, 
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
        indicator_name text,
        age_group text,
        sex text, 
        value integer,
        activity_report_form_id integer
    );

    for row in
        select * from data_entry_preexposureprophylaxis
    loop
        insert into temp_preexposureprophylaxis
            (indicator_name, age_group, sex, value, activity_report_form_id)
        values 
            ('referred_pep', '15_19', 'female', row.referred_pep_female_15_19, 
             row.activity_form_id),
            ('referred_pep', '20_24', 'female', row.referred_pep_female_20_24, 
             row.activity_form_id),
            ('referred_pep', '25_plus', 'female', row.referred_pep_female_25_plus, 
             row.activity_form_id),
            ('referred_pep', '15_19', 'male', row.referred_pep_male_15_19, 
             row.activity_form_id),
            ('referred_pep', '20_24', 'male', row.referred_pep_male_20_24, 
             row.activity_form_id),
            ('referred_pep', '25_plus', 'male', row.referred_pep_male_25_plus, 
             row.activity_form_id);
    end loop;

    return query
        select * from temp_preexposureprophylaxis;
end;
$$ language plpgsql;

