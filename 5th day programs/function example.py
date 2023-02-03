#example
def sample():
    print("great day")
    print("happy day")

sample()
print("today")
sample()

#multiplication(without argument without return value)
def multi():
    n1=int(input("number:"))
    n2=int(input("number:"))
    n3=int(input("number:"))
    prod=n1*n2*n3
    print(prod)
multi()

#another way of multiplication(without argument with return value)
def multi():
    n1=int(input("number:"))
    n2=int(input("number:"))
    n3=int(input("number:"))
    prod=n1*n2*n3
    return prod
res=multi()
print(res)

#with argument without return value
def multi(n1,n2,n3):
    prod=n1*n2*n3
    print(prod)
multi(3,4,5)

def multi(a,b,c):
    prod=a*b*c
    print(prod)
a=int(input("enter 1: "))
b=int(input("enter 2: "))
c=int(input("enter 3: "))
multi(a,b,c)

#with argument with return value
def multi(n1,n2,n3):
    prod=n1*n2*n3
    print(prod)
res=multi(3,4,5)
print(res)

def multi(a,b,c):
    prod=a*b*c
    return prod 
a=int(input("enter 1: "))
b=int(input("enter 2: "))
c=int(input("enter 3: "))
res=multi(a,b,c)
print(res)
