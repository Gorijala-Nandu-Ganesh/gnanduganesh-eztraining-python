def display():
    n=int(input("enter a number: "))
    if n==1:
        display()
    else:
        print('over')
display()
