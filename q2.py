dog = {} #Empty dictionary
dog.update({'name':'husky','color':'black','breed':'Siberian husky','Legs':4,'age':3});
student = { 'first_name':'Tejaswi Reddy', 'last_name':'Kallepu', 'gender':'F', 'age':23, 'marital_status':'Unmarried', 'skills':['Python','ML','Java'], 'country':'India', 'city':'Hyderabad', 'address':'Karimnagar'}
print(len(student))
print(student["skills"],type(student["skills"]))
student["skills"].append("SAP PI/PO")
student["skills"].append("SAP CPI")
print(student.keys())
print(student.values())
