a=10
try:
    b=int(input("Enter number: "))
    print("resource open")
    print(a/b)
except ZeroDivisionError as e:
    print("Please note, number can't be divided by zero")
except ValueError as e:
    print("Invalid input")
except Exception as e:
    print("Other error")
finally:
    print("Resource closed")
