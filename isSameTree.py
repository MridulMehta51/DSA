from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Perform a level-order traversal to convert the tree into a list
        def level_order_traversal(root):
            if not root:
                return []
            result = []
            queue = deque([root])
            while queue:
                node = queue.popleft()
                if node:
                    result.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    result.append(None)
            
            # Remove trailing None values (they represent extra empty nodes in the tree structure)
            while result and result[-1] is None:
                result.pop()
            
            return result
        
        # Compare both trees
        return level_order_traversal(p) == level_order_traversal(q)
