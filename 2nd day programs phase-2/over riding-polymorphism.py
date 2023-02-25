class vijayawada():
    def placename(self):
        print("vijayawada place name is KLU")
    def student(self):
        print("Yes-vijayawada")
    def which_year(self):
        print("3rd year")
class hyd():
    def placename(self):
        print("HYD placename is HYD-KLU")
    def student(self):
        print("Yes-HYD")
    def which_year(self):
        print("3rd year-HYD")
obj_vij=vijayawada()
obj_hyd=hyd()
for details in (obj_vij,obj_hyd):
    details.placename()
    details.student()
    details.which_year()
