def happy(n):
    s=r=0
    while(n>=0):
        for i in range(0,len(str(n))+1):
         r=n%10
         s=s+r**2
         n=n//10
        return s
n=int(input("enter a number: "))
res=n
while(res!=1 and res!=4):
    res=happy(res)
if res==1:
    print("happy number")
else:
    print("not a happy number")
