class Employe:
    
    increment = 1.5
    no_of_empl = 0
    
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employe.no_of_empl += 1
        
    def increase(self):
        self.salary = int(self.salary*self.increment)
        
    @classmethod
    def change_increment(cls,amount):
        cls.increment = amount
        
print(Employe.no_of_empl)
harry = Employe("Harry",44000)
rohan = Employe("Rohan",38000)
print(Employe.no_of_empl)
print()

# To implement classmethod
print(harry.salary)
Employe.change_increment(2)
harry.increase()
print(harry.salary)