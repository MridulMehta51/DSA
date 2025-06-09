# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        curr=head
        count=1
        while curr.next:
            curr=curr.next
            count+=1
        curr.next = head
        
        p=k%count
        
        breakcycle=count-p
        
        newstart=head
        for _ in range(breakcycle-1):
            newstart=newstart.next
        newhead=newstart.next

        newstart.next=None
        
        return newhead
            
        
