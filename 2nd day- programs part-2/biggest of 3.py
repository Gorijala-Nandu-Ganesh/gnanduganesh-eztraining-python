n1,n2,n3=int(input("enter n1:")),int(input("enter n2:")),int(input("enter n3:"))
if (n1>n2)&(n1>n3):
    print("n1 is the biggest")
elif (n2>n1)&(n2>n3):
    print("n2 is the biggest")
elif (n3>n1)&(n3>n2):
    print("n3 is the biggest")
elif (n1==n2)&(n1>n3):
    print("n1 and n2 are biggest")
elif (n3==n2)&(n3>n1):
    print("n3 and n2 are biggest")    
elif (n1==n3)&(n1>n2):
    print("n1 and n3 are biggest")
else:
    print("all are equal")
