# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def getListLen(self,head):
        length=0
        
        while head:
            length+=1
            head=head.next
        return length
        
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lenA=self.getListLen(head)
        
        if lenA<n:
            return head
        # if lenA==1:
        #     return
    
        ele=lenA-n
        curr=head
        i=1
        dummy=ListNode(0)
        dummy.next=head
        curr=dummy
        for _ in range(lenA-n):
            
        
            curr=curr.next
            
        curr.next=curr.next.next
        
        return dummy.next
        
        
