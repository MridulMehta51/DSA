# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        
        odd =head #1
        even=head.next #2
        
        evenhead=even #2
        
        while even and even.next:
            odd.next=even.next #1->3
            odd=odd.next # 3
            
            even.next=odd.next 
            even=even.next
            
        odd.next=evenhead
            
        return head
        
