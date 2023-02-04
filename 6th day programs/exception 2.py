a=10
b=1
try:
    print("resource open")
    print(a/b)
except Exception as e:
    print("Dont't give second number as zero")
finally:
    print("Resource closed")
