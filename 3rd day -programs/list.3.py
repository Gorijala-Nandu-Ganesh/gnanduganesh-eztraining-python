'''L=[1,2,3,4,5,6]
for i in  L:
   if (i%2==0):
    print(i)'''
#for user input
size=int(input("size"))
L=[]
for i in range(size):
    ele=int(input("element: "))
    L.append(ele)
print(L)
for j in L:
    if (j%2==0):
         print(j)
