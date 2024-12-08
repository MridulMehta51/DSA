# class TreeNode:
#     def __init__(self,root,left=None,right=None):
#         self.root=root
#         self.left= left
#         self.right= right
#     def __str__(self):
        
#         return str(self.root)
        
#     def preorder(self):
#         if not self:
#             return 
            
#         print(self.root)
#         if self.left:
#             self.left.preorder()
#         if self.right:
#             self.right.preorder()
        
#     def inorder(self):
#         if not self:
#             return
            
#         if self.left:
#             self.left.inorder()
                
#         print(self.root)
            
#         if self.right:
#             self.right.inorder()
#     def post(self):
#         if not self:
#             return
#         if self.left:
#             self.left.post()
#         if self.right:
#             self.right.post()
#         print(self.root)
               
# A = TreeNode(1)
# B = TreeNode(2)
# C = TreeNode(3)
# D = TreeNode(4)
# E = TreeNode(5)
# F = TreeNode(10)

# A.left = B
# A.right = C
# B.left = D
# B.right = E
# C.left = F

# print("Inorder")
# A.inorder()
# print("preorder")
# A.preorder()
# print("Post")
# A.post()


class TreeNode:
    def __init__(self,root,left=None,right=None):
        self.root=root
        self.left= left
        self.right=right
    
    def __str__(self):
        return str(self.root)

    def inorder(self):
        if not self:
            return 
        if self.left:
            self.left.inorder()

        print(self.root)

        if self.right:
            self.right.inorder()

    def preorder(self):
        if not self:
            return

        print(self.root)

        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    def postorder(self):
        if not self:
            return
        if self.left:
            self.left.postorder()  
        if self.right:
            self.right.postorder()
        print(self.root)

    def bfs(self):

        queue=[]
        queue.append(self)

        while queue:
            print("before",[str(node) for node in queue])
            node=queue.pop(0)
            print(node)
            

            if node.left:
                queue.append(node.left)
               
            if node.right:
                queue.append(node.right)


        


    
A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)
G= TreeNode(11)
H = TreeNode(12)
I = TreeNode(13)
J = TreeNode(14)
K = TreeNode(15)
L = TreeNode(16)
M = TreeNode(17)
N=TreeNode(18)
O=TreeNode(19)
A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
C.right=G
D.left =H 
D.right=I
E.left =J
E.right=K
F.left = L
F.right=M
G.left = N
G.right=O

    
# print(str(A))
# print("inorder")
# A.inorder()
# print("pre")
# A.preorder()
# print("Post")
# A.postorder()
print("bfsbfsbfs")
A.bfs()
