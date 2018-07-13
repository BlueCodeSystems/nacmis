-- 

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
             row.activity_form_id)
            ;
    end loop;

    return query
        select * from temp_sex_workers;
end;
$$ language plpgsql;

