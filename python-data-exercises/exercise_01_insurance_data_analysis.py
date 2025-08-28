medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# to replace '#' with '$'
updated_medical_data = medical_data.replace('#', '$')

# to print out a sentance telling the number of medical records in the data.
num_records = 0
for character in updated_medical_data:
  if character == "$":
    num_records += 1
print('There are {} medical records in the data.'.format(num_records))

# to split data between ';'
medical_data_split = updated_medical_data.split(';')

# to clean up ','
medical_records = []
for record in medical_data_split:
  medical_records.append(record.split(','))

# to clean up whitespace
medical_records_clean = []
for record in medical_records:
  record_clean = []
  for item in record:
    record_clean.append(item.strip())
  medical_records_clean.append(record_clean)
print(medical_records_clean)

# to print out names in upper case
for record in medical_records_clean:
  print(record[0].upper())

# to seperately print out list of names, ages...
names = []
ages = []
bmis = []
insurance_costs = []
for record in medical_records_clean:
  names.append(record[0])
  ages.append(record[1])
  bmis.append(record[2])
  insurance_costs.append(record[3])
print(names, ages, bmis, insurance_costs)

# to calculate average bmi
total_bmi = 0
for bmi in bmis:
  total_bmi += float(bmi)
average_bmi = total_bmi / len(bmis)
print('Average BMI: {}'.format(average_bmi))

# to calculate average insurance cost
total_insurance_cost = 0
for insurance_cost in insurance_costs:
  total_insurance_cost += float(insurance_cost.strip('$'))
average_insurance_cost = total_insurance_cost / len(insurance_costs)
print('Average insurance cost: {}'.format(average_insurance_cost))

# to print seperate output as sentences
for i in range(len(medical_records_clean)):
  print('{} is {} years old with a BMI of {} and an insurance cost of {}.'.format(names[i], ages[i], bmis[i], insurance_costs[i]))