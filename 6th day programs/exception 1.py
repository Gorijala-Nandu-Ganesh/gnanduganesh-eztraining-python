a=100
b=0
try:
    print(a/b)
except Exception :
    print("Please note, number can't be divided by zero")
print("bye")

#with e
a=100
b=0
try:
    print(a/b)
except Exception as e:
    print("Please note, number can't be divided by zero")
print("bye")
