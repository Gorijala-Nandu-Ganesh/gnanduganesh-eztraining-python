class Employee:
    def __init__(self,name,id):
        self.id=id
        self.name=name
    def display(self):
        print("ID: %d \nName: %s" %(self.id,self.name))

        
emp1 = Employee("John",101)
emp2 = Employee("David",102)


emp1.display()
emp2.display()
