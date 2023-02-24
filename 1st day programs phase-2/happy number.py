n=int(input("enter a number: "))
while(n>=10):
   s=0
   for i in range(0,len(str(n))+0):
       r=n%10
       s=s+(r*r)
       n=n//10
   n=s
if n==1:
    print("given number is a happy number")
else:
    print("given number is not a happy number")    
