
class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None

    def start(self,head,data):
        newNode=Node(data)
        if head is None:
            return newNode
        else:
            newNode.next=head
            return newNode
        

    def end(self,head,data):
        newNode=Node(data)

        if head is None:
            return newNode
        
        current =head
        while current.next:
            current=current.next
        current.next = newNode
        return head

        



    def display(self,head):

        current=head

        while current:
            print(current.data, end="-->")
            current= current.next
        print("None")


head=None

nodeop=Node(None)

head= nodeop.start(head,1)
head= nodeop.start(head,2)
head= nodeop.start(head,3)
head= nodeop.start(head,4)
head= nodeop.start(head,5)

head= nodeop.end(head,6)
head= nodeop.end(head,7)
head= nodeop.end(head,8)

nodeop.display(head)        
