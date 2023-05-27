class Employee:
    company = "Google"
    
harry = Employee()
rajni = Employee()
print(harry.company)
print(rajni.company)
# To change the company attribute which is inside class...We do the below:
Employee.company = "YouTube"
print("Changed to ",harry.company)
print("Changes to ",rajni.company)
#you can change them during the program
