# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        
        slow=head
        fast=head.next
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
        curr=slow.next
        prev=None
        
        while curr:
            temp=curr.next
            curr.next =prev
            prev=curr
            curr=temp
        while prev:
            if prev.val!=head.val:
                return False
            prev,head=prev.next,head.next
            
        return True
        
        
        
