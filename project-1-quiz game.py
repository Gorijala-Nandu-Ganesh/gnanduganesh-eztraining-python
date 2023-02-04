q1="""which team won PKL 2022?
a.Jaipur Pink Panters
b.Patna Pirates
c.Dabang Delhi
d.Puneri Paltans"""
q2="""what is the value of 2*5+5*2?
a.21
b.22
c.19
d.20"""
q3="""who is 1st prime minister of India?
a.Jawaharlal Nehru
b.Mahatma Gandhi
c.Subash Chandra Bose
d.Godse"""
q4="""who is the captain of RCB in 2021 IPL?
a.Dhoni
b.Virat Kohli
c.Rohit Sharma
d.David Warner"""
q5="""who is the father of computer?
a.Guido Van Rossum
b.Charles Babbage
c.Wright brothers
d.Thomas Alwa Edison"""

questions={q1:"a",q2:"d",q3:"a",q4:"b",q5:"b"}
name=input("Hi whats your name ")
print("Hello",name,"welcome to the quiz")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("Do you want to skip this quiz(yes/no)")
    if flag1=="yes":
        continue
    ans=input("enter your answer")
    if ans==questions[i]:
       print("Wow! you gat one point")
       score=score+1
       print("your current score is ",score)
    else:
       print("wrong answer, you lost one mark")
       score=score-1
       print("your current score is ",score)
    flag2=input("Do you want to quiz? type (yes/no)")
    if flag2=="yes":
        break
print("Your total score is ",score)
