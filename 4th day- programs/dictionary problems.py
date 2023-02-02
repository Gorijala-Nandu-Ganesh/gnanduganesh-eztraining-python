d={n:n*n for n in range(1,5)}
print(d)

#calculating product price for 5 units
old={'rice':60,'dhaal':120,'oil':150}
new={product:price*5 for (product,price) in old.items()}
print(new)

#with checks
real={'sam':24,'angel':18,'kumar':35}
now={name:age for (name,age) in real.items() if age>20}
print(now)
