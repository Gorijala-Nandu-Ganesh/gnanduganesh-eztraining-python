#private
class encap:
    __a=10
    print(__a)
    def encapfunction(self):
        print("Encap function")
        print(self.__a)
obj=encap()
obj.encapfunction()
print(obj.__a)#will throw error because 'a' is private, can't be accessed outside class
