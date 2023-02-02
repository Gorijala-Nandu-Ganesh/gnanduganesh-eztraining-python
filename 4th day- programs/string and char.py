#my logic
'''m=input(str)
n=input(chr)
if n in m:
    print("the character is there")
else:
    print("the character is not there")'''
    
#iteration logic
s=input("enter: ")
char=input()
for i in s:
    if i==char:
        flag=1
    else:
        flag=0
if flag==1:
    print("present")
else:
    print("not present")
