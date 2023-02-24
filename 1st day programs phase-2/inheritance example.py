class A:
    n=30
class B(A):
    def calc(self):
        c=self.n+70
        print(c)
obj=B()
obj.calc()
