class PatientData:
    height_inches = 0
    weight_pounds = 0
    
patient = PatientData()
print('Patient data (before):', end=' ')
print(patient.height_inches, 'in,', end=' ')
print(patient.weight_pounds, 'lbs')


patient.height_inches = int(input())
patient.weight_pounds = int(input())

print('Patient data (after):', end=' ')
print(patient.height_inches, 'in,', end=' ')
print(patient.weight_pounds, 'lbs')