'''
Show all of the patients grouped into weight groups.
Show the total amount of patients in each weight group.
Order the list by the weight group decending.

For example, if they weight 100 to 109 they are placed in the 100 weight group, 110-119 = 110 weight group, etc.
'''

'''
select count(p.weight) as patients_count,floor(weight/10) * 10 as weight_group from patients p
group by weight_group
order by weight_group desc
'''

'''
Show patient_id, weight, height, isObese from the patients table.

Display isObese as a boolean 0 or 1.

Obese is defined as weight(kg)/(height(m)2) >= 30.

weight is in units kg.

height is in units cm.
'''

'''
select patient_id,weight,height,(case
when (weight/power((height/100.0),2))>=30 then 1 ELSE 0 END) as isObese from patients 
'''

'''
Show patient_id, first_name, last_name, and attending doctor's specialty.
Show only the patients who has a diagnosis as 'Epilepsy' and the doctor's first name is 'Lisa'

Check patients, admissions, and doctors tables for required information. 
'''

'''
select p.patient_id,p.first_name,p.last_name,d.specialty from patients p, doctors d, admissions a
where a.patient_id=p.patient_id and a.attending_doctor_id=d.doctor_id and diagnosis='Epilepsy' and d.first_name='Lisa'
'''

'''
All patients who have gone through admissions, can see their medical documents on our site. Those patients are given a temporary password after their first admission. Show the patient_id and temp_password.

The password must be the following, in order:
1. patient_id
2. the numerical length of patient's last_name
3. year of patient's birth_date
'''

'''
select distinct p.patient_id,concat(p.patient_id,len(p.last_name),year(p.birth_date)) from patients p
right join admissions a on p.patient_id=a.patient_id
'''

'''
Each admission costs $50 for patients without insurance, and $10 for patients with insurance. All patients with an even patient_id have insurance.

Give each patient a 'Yes' if they have insurance, and a 'No' if they don't have insurance. Add up the admission_total cost for each has_insurance group.
'''

'''
select (case
        when patient_id%2=0 then 'yes'
        else 'no' end) as Insurance, sum(case
                                      WHEN patient_id%2=0 then 10
                                      else 50 end) as cost 
                                      from admissions
                                      group by Insurance
'''

'''
Show the provinces that has more patients identified as 'M' than 'F'. Must only show full province_name
'''

'''
select p.province_name from province_names p, patients pat
using(province_id)
group by province_id
HAVING sum(pat.gender='M')>SUM(pat.gender='F')
'''

'''
We are looking for a specific patient. Pull all columns for the patient who matches the following criteria:
- First_name contains an 'r' after the first two letters.
- Identifies their gender as 'F'
- Born in February, May, or December
- Their weight would be between 60kg and 80kg
- Their patient_id is an odd number
- They are from the city 'Kingston'
'''

'''
select * from patients
where first_name like '__r%' and gender='F' and (month(birth_date) in (2,5,12)) and (weight between 60 and 80)
and patient_id%2=1 and city='Kingston'
'''

'''
Show the percent of patients that have 'M' as their gender. Round the answer to the nearest hundreth number and in percent form.
'''

'''
select CONCAT(ROUND(SUM(gender='M')/CAST(count(*) as float)*100,2),'%') from patients
'''

'''
For each day display the total amount of admissions on that day. Display the amount changed from the previous date.
'''

'''
select t.admission_date,count(t.patient_id), count(tom.patient_id) - COUNT(t.patient_id) 
from admissions t, (select patient_id,(LAG(admission_date,1) over ()) as tommorow from admissions) tom
where tom.tommorow=t.admission_date
group by t.admission_date
limit 5

--lead(admission_date,1) over () as tommorow, admission_date as today

'''

'''

select t.admission_date,count(t.patient_id),COUNT(admission_date) - LAG(COUNT(admission_date)) OVER (ORDER BY admission_date) from admissions t
group by admission_date
'''

'''
Sort the province names in ascending order in such a way that the province 'Ontario' is always on top.
'''

'''
select province_name from province_names
order by (CASE when province_name='Ontario' then 'Ontario' END) DESC,province_name
'''

'''
We need a breakdown for the total amount of admissions each doctor has started each year. Show the doctor_id, doctor_full_name, specialty, year, total_admissions for that year.
'''

'''
select d.doctor_id,CONCAT(d.first_name,' ',d.last_name),d.specialty,YEAR(a.admission_date),COUNT(a.admission_date)
from doctors d, admissions a
where d.doctor_id=a.attending_doctor_id
group by YEAR(a.admission_date),d.doctor_id
order by d.doctor_id
'''