class Employee:
    company = "Google"
    
    def __init__(self, name, salary, work):
        self.name = name
        self.salary = salary
        self.work = work
        print()
        print("Hi Chuthiyon...!")
        print("This is ",self.name)
        print()
        
    def getSalary(self):
        print(self.name," is been paid ",self.salary," becouse he is the ",self.work," of the company ",self.company)
        
    def display(self):
        print()
        print("The name of the Emploee is: ",self.name)
        print("The salary of the Emploee is: ",self.salary)
        print("The work of the Emploee is: ",self.work)
        
emp = Employee("Akash Babu", 1000000000, "CEO")
emp.display()
emp.getSalary()
