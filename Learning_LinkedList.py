class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Learning_LinkedList():
    def create_linkedlist(self, n_terms): # 5
        i = 1
        self.head = ListNode(val=i**2)

        temp = self.head
        while(i < n_terms):
            i += 1
            temp2 = ListNode(val=i**2)
            temp.next = temp2
            temp = temp2
        
        print("Linked List Created")
        return self.head
    
    def print_linkedl
