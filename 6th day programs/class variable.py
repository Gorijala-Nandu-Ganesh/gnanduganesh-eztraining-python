class computer():
    a=10
    b=20
    print("Class variable inside class",a)
    def config(self):
        c=100
        print("Yes")
        print("Instance access",self.b)
lenova=computer()
print(lenova.a)
print(lenova.a+lenova.b)
dell=computer()
print("dell",dell.a)
lenova.config()


