
class ListNode:
    def __init__(self,val=0):
        self.val=val
        self.next=None
class MyLinkedList(object):

    def __init__(self):
        self.head=ListNode()
        self.size=0
       

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """#1->2->3
        #0->1->2->3
        if (index>=self.size):
            return -1
        curr=self.head.next
       
        for _ in range(index):
            curr=curr.next
           
        return curr.val
           

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        Node=ListNode(val)
        Node.next=self.head.next
        self.head.next=Node
        self.size+=1
       
       

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        Node=ListNode(val)
        curr=self.head
       
        while curr.next:
            curr=curr.next
        curr.next=Node
        self.size+=1
             
         
    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None 0->1->2->2.5->3->4
        """#1->2->3->4
        Node=ListNode(val)
        if (index>self.size):
            return None
        curr= self.head
        for _ in range(index):
            curr=curr.next
           
        Node.next=curr.next
        curr.next=Node
        self.size+=1
       
       

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """ #0->1->2->3
        if (index>=self.size):
            return None
        curr=self.head
       
        for _ in range(index):
            curr=curr.next
       
        curr.next=curr.next.next
        self.size-=1
           
