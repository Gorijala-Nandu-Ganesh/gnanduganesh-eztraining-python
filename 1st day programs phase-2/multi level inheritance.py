#one parent and one child class
class grandparent:
    def display(self):
        print("grandparent class")
class parent(grandparent):
    def show(self):
        print("parent class")
class child(parent):
    def printing(self):
        print("child class")
c=child()      #c is object for child class....object
c.display()
c.show()
c.printing()
