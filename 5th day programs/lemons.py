def lemons():
    n=int(input("enter number of lemons: "))
    if n==21:
        print("lemons are enough")
    elif n>21:
        m=n-21
        print(m,"lemons are excess ")
    elif n<21:
        p=21-n
        print(p,"lemons are not sufficient ")
lemons()
        
