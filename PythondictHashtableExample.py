employee = {
    'name': 'John Doe',
    'age': 36,
    'position': 'Business Manager.'
}

print (f"The name of the employee is {employee['name']}")
employee['position'] = 'Software Engineer'
print (f"The position of {employee['name']} is {employee['position']}")
employee['age'] = '36'
print (f"The Age of {employee['name']} is {employee['age']}")

employee.clear()

print (employee)