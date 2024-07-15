employee = {"name": "Jhon" , "age": 29, "salary" :25000,"company" :"GOOGLE"}
print(type(employee))
print("printing employee data ....")
print(employee)

print("deleting some of the employee data")
del employee["name"]
del employee["company"]

print("printing the modified information")
print(employee)

print("deleting the dictionary: employee")
del employee
 
print("lets try to print it again")
print(employee)