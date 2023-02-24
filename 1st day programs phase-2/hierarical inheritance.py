#one base class and multiple child class
#objects should be created for child class individuals
class parent:                         #base class
    def pdisplay(self):               #method
        print("parent class")
class child1(parent):                 #derived class-1
    def c1show(self):
        print("child1 class")
class child2(parent):                 #derived class-2
    def c2show(self):
        print("child2 class")
c1=child1()
c1.c1show()
c1.pdisplay()
c2=child2()
c2.c2show()
c2.pdisplay()
