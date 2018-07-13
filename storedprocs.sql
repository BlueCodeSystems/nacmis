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

