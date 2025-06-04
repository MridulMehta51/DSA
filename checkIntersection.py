
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getListLength(self, head):
        length = 0
        while(head):
            length += 1
            head = head.next
           
        return length
   
    def getListDict(self, head):
        nodes = {}
        while(head):
            nodes[head] = True
            head = head.next
       
        return nodes
   
    def checkIntersection(self, head, nodes):
        while(head):
            if head in nodes:
                return head
            head = head.next
       
        return
       
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
#         lenA, lenB = self.getListLength(headA), self.getListLength(headB)

#         if(lenA >= lenB):
#             nodes = self.getListDict(headB)
#             return self.checkIntersection(headA, nodes)
       
#         nodes = self.getListDict(headA)
#         return self.checkIntersection(headB, nodes)
       
        nodes = self.getListDict(headA)
        return self.checkIntersection(headB, nodes)
