#prg-display date month
import datetime
a=datetime.datetime.now()
print(a)
sv=a.strftime("%y")
fv=a.strftime("%Y")
print("Year short version ",sv)
print("Year full version ",fv)
