n=int(input("enter a number:"))
if (n<0)&(n%2==0):
    print("its even negative number")
elif (n>0)&(n%2==0):
    print("its even positive number")
elif (n<0)&(n%2==1):
    print("its odd negative number")
elif (n>0)&(n%2==1):
    print("its odd positive number")
