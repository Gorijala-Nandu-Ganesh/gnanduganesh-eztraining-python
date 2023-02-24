#two classes-one child-like mom,dad----child
#inherit properties of mom and dad
class mom:                              #BASE CALSS-1
    def mdisplay(self):
        print("mom class")
class dad:                              #BASE CLASS-2
    def ddisplay(self):
        print("dad class")
class child(mom,dad):                   #DERIVED (OR) INHERITED
    def cdisplay(self):
        print("child class")
c1=child()
c1.cdisplay()
c1.mdisplay()
c1.ddisplay()
        
