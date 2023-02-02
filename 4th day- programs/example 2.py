Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
z='bluegreen'
z.center(8,'*')
'bluegreen'
z.center(1,'*')
'bluegreen'
z.center(40,'$')
'$$$$$$$$$$$$$$$bluegreen$$$$$$$$$$$$$$$$'
z.center(9,'*')
'bluegreen'
z.center(10,'*')
'bluegreen*'
z.center(11,'*')
'*bluegreen*'
z.endswith('n',0.len(z))
SyntaxError: invalid decimal literal
z.endswith('n',0,len(z))
True
z.endswith('n',0,len(z-1))
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    z.endswith('n',0,len(z-1))
TypeError: unsupported operand type(s) for -: 'str' and 'int'
z.endswith('n',5,len(z))
True
z.endswith('i',0,len(z))
False
z.endswith('n',8,len(z))
True
z.endswith('n',9,len(z))
False
z.endswith('n',4,len(z))
True
find('e',0,len(z))
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    find('e',0,len(z))
NameError: name 'find' is not defined
z.find('e',0,len(z))
3
z.find('n',0,len(z))
8
z.index('e',3,len(z))
3
z.index('g',3,len(z))
4
k='hhhhhhhgghhhghhhghghhghhhhghhhhhhghghhghghhhhhghhhghhhhhhhhghghhhhgghghhgghhhhhhhhhhhhgghhhhhhhhggghgghhhhhhhhhhhhhhhghhhggggghghgghggggghgghggghgggggghhhgghhgggghhgghgghgggghhhggghggggggh'
k.count('g')
75
k.count('h')
113
m=30
m
30
m=m+m
m
60
id(m)
2083028731984
m=m-m
m
0
id(m)
2083028730064
L=[1,2,3,4]
l
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    l
NameError: name 'l' is not defined. Did you mean: 'L'?
LK
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    LK
NameError: name 'LK' is not defined. Did you mean: 'L'?
L
[1, 2, 3, 4]
L.append(10)
L
[1, 2, 3, 4, 10]
id(L)
2083045437184
L.extend([10,11,12])
L
[1, 2, 3, 4, 10, 10, 11, 12]
id(L)
2083045437184
id(2)
2083028730128
