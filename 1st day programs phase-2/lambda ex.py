L=[2,4,6,8,10,12,14]
r=map(lambda n:pow(n,(1/2)),L)
print(list(r))


#another method
n=int(input("enter a number: "))
a=[]
for i in range(2,n+1,2):
      print(i)
      r=i**(1/2)
      a.append(r)
print(a)
