Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
n="hii i'am "hello""
SyntaxError: invalid syntax
n="hii i""am"""
n
'hii iam'
m="hii\i\am"
m
'hii\\i\x07m'
y="hii i\'am'"
y
"hii i'am'"
"hii i am ""nandu"""
'hii i am nandu'
"hii i am """"nanduganesh"""""
'hii i am nanduganesh'
print(a>b)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(a>b)
NameError: name 'a' is not defined
print('a'>'b')
False
print('a'<'b')
True
max("abc")
'c'
max('a','b','c')
'c'
n=hai
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    n=hai
NameError: name 'hai' is not defined
n="hii"
c.upper(n)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    c.upper(n)
NameError: name 'c' is not defined
s.upper(n)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    s.upper(n)
NameError: name 's' is not defined
n.upper()
'HII'
s='HELLo"
SyntaxError: unterminated string literal (detected at line 1)
s='HELlO'
s.lower()
'hello'
s.casefold()
'hello'
n.capitalize
<built-in method capitalize of str object at 0x0000023B4EC509B0>
y='bye'
y.capitalize()
'Bye'
y.count(b)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    y.count(b)
NameError: name 'b' is not defined
y.count('b')
1
y.count('B')
0
z='hii iam happy'
z.count('p',len(z))
0
z.count('p',1,len(z))
2
z.count('p',9,len(z))
2
z.count('p',12,len(z))
0
z.count('p',11,len(z))
1
z.count('h',0,len(z))
2
z.count('h',1,len(z))
1
e='bluegreen'
e.strip('u')
'bluegreen'
e.strip()
'bluegreen'
e.strip e.split('u')
SyntaxError: invalid syntax
e.split('u')
['bl', 'egreen']
e.strip
<built-in method strip of str object at 0x0000023B4EC52570>
e.centre(8,'$')
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    e.centre(8,'$')
AttributeError: 'str' object has no attribute 'centre'. Did you mean: 'center'?
