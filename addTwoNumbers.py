# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry=0
        dummy=ListNode(0)
        temp=dummy
        
        while l1 or l2 or carry:
            if not l1 and l2:
                l1 = ListNode(0)
            if l1 and not l2:
                l2 = ListNode(0)
            if not l1 and not l2 and carry:
                l1=ListNode(0)
                l2=ListNode(0)
            total=l1.val+l2.val+carry 
            digit=total%10
            carry=total//10
            temp.next=ListNode(digit)
            temp=temp.next
                
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
            
        return dummy.next
                
