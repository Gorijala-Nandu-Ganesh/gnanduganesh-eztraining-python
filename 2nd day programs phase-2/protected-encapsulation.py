#protected
class encap:
    _a=10
    c=20
    def encapfunction(self):
        _b=200
        print("Encap function accessing protected")
        print(self._a+10)
obj=encap()
print(obj._a)
obj.encapfunction()
print(obj.c)
