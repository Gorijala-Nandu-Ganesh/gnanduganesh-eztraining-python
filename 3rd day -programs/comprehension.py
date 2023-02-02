numbers=[numbers for numbers in "Good Afterenoon"]
print(numbers)

L=["hyderabad","vizag","chennai","vijayawada"]
city=[]
for n in L:
    if "v" in n:
        city.append(n)
print(city)

L1=[2**x for x in range(2,10)]
print(L1)

L2=[a for a in range(200,100,-20)]
print(L2)

L3=[1,2,3,4,5,6]
L4=[i for i in L3 if(i<5)]
print(L4)
