# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        total_sum = 0
        stack = [(root, root.val)]  # Stack holds tuples of (node, current number formed)
        
        while stack:
            node, current_val = stack.pop()
            
            # If it's a leaf node, add the current number to the total sum
            if not node.left and not node.right:
                total_sum += current_val
            
            # If left child exists, push it onto the stack
            if node.left:
                stack.append((node.left, current_val * 10 + node.left.val))
            
            # If right child exists, push it onto the stack
            if node.right:
                stack.append((node.right, current_val * 10 + node.right.val))
        
        return total_sum
