#one parent and one child class

class parent:             #BASE CLASS
    def display(self):
        print("parent calss")

#DERIVED CLASS

class child(parent):      #child inherits properties
    def show(self):
        print("child class")
c=child()                 #c is object for child class
c.display()
c.show()
