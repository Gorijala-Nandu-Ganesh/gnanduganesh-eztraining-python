n=list(map(int,input("enter: ").split()))
print(n)
x=1
y=0
for i in n:
    x=x*i
    y=y+i
if x<=750:
    print("prod",x)
else:
    print("sum",y)
