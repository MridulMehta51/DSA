# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr=[]
        def inorder(node):
            if not node:
                return 
            if node:
                arr.append(node)
                inorder(node.left)
                
                inorder(node.right)
        inorder(root)
        for i in range(1,len(arr)):
            arr[i-1].left=None
            arr[i-1].right=arr[i]
        if arr:
            arr[-1].left=None
            arr[-1].right=None
            

        
