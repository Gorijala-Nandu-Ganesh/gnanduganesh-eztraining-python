def digits(n):
     sum=0
     while n!=0:
         rem=n%10
         sum=sum+rem
         n=n//10
     return sum
n=int(input("enter a number: "))
res=digits(n)
print(res)
