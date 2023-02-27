class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CreateList:
    def __init__(self):
        self.head=Node(None)
        self.tail=Node(None)
        self.head.next=self.tail
        self.tail.next=self.head
    #Adding node at end of LL
    def add(self,data):
        newNode=Node(data)
        #Is empty?
        if self.head.data is None:
            self.head=newNode
            self.tail=newNode
            newNode.next=self.head
        else:
            self.tail.next=newNode
            self.tail=newNode
            #It is CLL so tail will point to head
            self.tail.next=self.head
        def display(self):
            current=self.head
            if self.head is None:
                print("List is empty")
                return
            else:
                print("Nodes of circular linkedlist: ")
                print(current.data,"-->")
                while(current.next!=self.head):
                    current=current.next
                    print(current.data,"-->")
class CircularLinkedList:
    c1=CreateList()
    c1.add("H")
    c1.add("E")
    c1.add("L")
    c1.add("L")
    c1.add("O")
    c1.display()
