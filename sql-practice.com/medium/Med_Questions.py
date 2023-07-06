'''Show patient_id and first_name from patients
where their first_name start and ends with 's' and
is at least 6 characters long.'''

'''
SELECT patient_id,first_name FROM patients
where first_name like 's%s' and len(first_name)>=6
'''

'''Show unique birth years from patients and order them by ascending.'''

'''SELECT distinct year(birth_date) from patients
order by birth_date asc'''

'''Select first names that only appear once'''

'''SELECT first_name from patients
group by first_name
having count(first_name)=1
'''

'''Show patient_id, first_name, last_name from patients whos diagnosis is 'Dementia'.

Primary diagnosis is stored in the admissions table.'''

'''SELECT p.patient_id, p.first_name, p.last_name from patients p, admissions a
using(patient_id)
where a.diagnosis like 'Dementia%'
'''

'''Display every patient's first_name.
Order the list by the length of each name and then by alphbetically'''

'''select first_name from patients
order by len(first_name),first_name'''

'''
Show the total amount of male patients and the total amount of female patients in the patients table.
Display the two results in the same row.
'''

'''select
SUM(gender='M') as male_count,sum(gender='F') as female_count
from patients'''

'''Show first and last name, allergies from patients which have allergies to either 'Penicillin' or 'Morphine'. Show results ordered ascending by allergies then by first_name then by last_name.'''

'''select first_name,last_name,allergies from patients
where allergies like 'Penicillin' or allergies LIKE 'Morphine'
order by allergies,first_name,last_name'''

'''
Show patient_id, diagnosis from admissions. Find patients admitted multiple times for the same diagnosis.
'''

'''select distinct a.patient_id,a.diagnosis from admissions a,admissions b
using(patient_id)
where a.diagnosis=b.diagnosis and a.admission_date<>b.admission_date

'''


'''Show the city and the total number of patients in the city.
Order from most to least patients and then by city name ascending.'''

'''
select city,COUNT(*) as total from patients
group by city
order by total desc,city asc
'''

'''
Show first name, last name and role of every person that is either patient or doctor.
The roles are either "Patient" or "Doctor"
'''

'''
select  p.first_name,p.last_name,'Patient' as role from patients p
union all
select  d.first_name,d.last_name,'Doctor' as role from doctors d
'''

'''Show all allergies ordered by popularity. Remove NULL values from query.'''

'''
select allergies,count(allergies) as total_occurences from patients
group by allergies
having total_occurences<>0
order by total_occurences desc
'''

'''Show all patient's first_name, last_name, and birth_date who were born in the 1970s decade. Sort the list starting from the earliest birth_date.'''

'''
select first_name,last_name,birth_date from patients
where year(birth_date)>=1970 and year(birth_date)<1980
order by birth_date
'''

'''We want to display each patient's full name in a single column. Their last_name in all upper letters must appear first, then first_name in all lower case letters. Separate the last_name and first_name with a comma. Order the list by the first_name in decending order
EX: SMITH,jane'''

'''SELECT concat(upper(last_name),',',lower(first_name)) from patients
order by first_name desc'''

'''
Show the province_id(s), sum of height; where the total sum of its patient's height is greater than or equal to 7,000.'''

'''select province_id, sum(height) as total_height from patients
group by province_id
having total_height>=7000'''

'''Show the difference between the largest weight and smallest weight for patients with the last name 'Maroni''''

'''
Select (Max(weight)-Min(weight)) from patients
where last_name='Maroni'
'''

'''Show all of the days of the month (1-31) and how many admission_dates occurred on that day. Sort by the day with most admissions to least admissions.'''

'''
Select DAY(admission_date) as mday, count(admission_date) as cmday from admissions
group by day(admission_date)
order by cmday desc

'''


'''Show all columns for patient_id 542's most recent admission_date.'''

'''Select patient_id,admission_date,discharge_date,diagnosis,attending_doctor_id from admissions
where patient_id=542
order by admission_date desc
limit 1
'''

'''
Show patient_id, attending_doctor_id, and diagnosis for admissions that match one of the two criteria:
1. patient_id is an odd number and attending_doctor_id is either 1, 5, or 19.
2. attending_doctor_id contains a 2 and the length of patient_id is 3 characters.
'''

'''
select patient_id,attending_doctor_id,diagnosis from admissions
where (MOD(patient_id,2)=1 and attending_doctor_id in (1,5,19)) or (attending_doctor_id like '%2%' and len(patient_id)=3)
'''


