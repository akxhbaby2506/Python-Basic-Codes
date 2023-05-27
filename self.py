class Employee:
    company = "Google"
    def display_salary(self):
        print("salary for the employee working in ",self.company ," is ",self.salary)
        
Akash = Employee()
Akash.salary = 100000000000000
Akash.display_salary()