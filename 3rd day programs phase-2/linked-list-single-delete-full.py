# while creating LL  we gonna do it in ascending order
# one prg multiple concept :
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        current = self.head
        if not current:
            print('list is empty.')
        else:
            print('start:' , end=' ')
        while current:
            print(current.data, end =' -> ')
            current = current.next
        print('end.')

    def insert(self,data):
        new_node = Node(data)

        #if the linked list is empty
        if self.head is None:
            self.head = new_node

        # if the data is smaller than the head
        elif self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node

        else:
            # locate  node before the insertion point :
            current = self.head
            while current.next and new_node.data > current.next.data:
                current = current.next

            #insertion
                new_node.next =current.next
                current.next = new_node

    def delete(self,key):
        #if the list is empty
        if self.head is None:
            print('Delete error :the list is empty')
            return
        #if the key is in head
        if self.head.data == key:
            self.head = self.head.next
            return

        # find position of first occurrence of the
        current = self.head
        while current:
            if current.data == key:
                break
            previous = current
            current = current.next

# name is python special variable
if __name__=='__main__':
    # create an object
    LL = LinkedList()
    print('')
    #insert some nodes
    LL.insert(23)
    LL.insert(87)
    LL.insert(8)
    LL.insert(30)
    LL.insert(90)


    LL.printList()
    LL.delete(8)
    LL.delete(87)
    LL.delete(90)
    LL.printList()












            
        

        
