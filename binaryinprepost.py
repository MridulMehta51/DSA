class TreeNode:
    def __init__(self,root,left=None,right=None):
        self.root=root
        self.left= left
        self.right= right
    def __str__(self):
        
        return str(self.root)
        
    def preorder(self):
        if not self:
            return 
            
        print(self.root)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
        
    def inorder(self):
        if not self:
            return
            
        if self.left:
            self.left.inorder()
                
        print(self.root)
            
        if self.right:
            self.right.inorder()
    def post(self):
        if not self:
            return
        if self.left:
            self.left.post()
        if self.right:
            self.right.post()
        print(self.root)
            
            
    
        
        
A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

print("Inorder")
A.inorder()
print("preorder")
A.preorder()
print("Post")
A.post()
