'''L1=['a','b','c']
L2=[1,2,3]
d={a:b for (a,b) in zip(L1,L2)}
print(d)'''

#students marks to percentage
students=['kishore','hii','hello','sai','ravi']
marks=[455,478,486,459,476]
d={students:(marks/500)*100 for (students,marks) in zip(students,marks)}
print("percentages= ",d)

