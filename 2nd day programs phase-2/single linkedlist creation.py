#CREATING A NODE-Declaration and Definition
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head #temp=first node
            while temp:
                print(temp.data,"->",end=" ")
                #temp data means first nodes data
                temp=temp.next#establishing link
obj=singlelinkedlist()
#Node creation initialising
n=Node(10)      #so n.data in Node class will be 10
obj.head=n      #assigning first node as head
n1=Node(20)
obj.head.next=n1#next node value
n2=Node(30)
n1.next=n2
obj.display()

