from collections import deque;

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

    def __str__(self):
        return str(self.val)
    
A=TreeNode(1)
B=TreeNode(2)
C=TreeNode(3)
D=TreeNode(4)
E=TreeNode(5)
F=TreeNode(10)

A.left=B
A.right=C
B.left=D
B.right=E
C.left=F
print(A)

def inOrder(node):
    if not node:
        return
    
    inOrder(node.left)
    print(node)
    inOrder(node.right)

inOrder(A)

def preOrder(node):
    if not node:
        return 
    print(node)
    preOrder(node.left)
    preOrder(node.right)

preOrder(A)

def preOrder_iter(node):
    stk=[node]
    while stk:
        node=stk.pop()
        print(node)
        if node.right:
            stk.append(node.right)
        if node.left:
            stk.append(node.left)
preOrder_iter(A)

def level_order(node):
    q=deque()
    q.append(node)

    while q:
        node=q.popleft()
        print(node)

        if node.left: q.append(node.left)
        if node.right:q.append(node.right)
level_order(A)

def search(node,target):
    if not node:
        return False
    
    if node.val == target:
        return True
    return search(node.left,target) or search(node.right,target)

print(search(A,6))

A2=TreeNode(5)
B2=TreeNode(3)
C2=TreeNode(8)
D2=TreeNode(2)
E2=TreeNode(4)
F2=TreeNode(7)

A2.left=B2
A2.right=C2
B2.left=D2
B2.right=E2
C2.Left=F2
print(A2)


def searchBST(node,target):
    if not node:
        return False
    if node.val==target:
        return True
    
    if target<node.val:
        return searchBST(node.left,target)
    if target>node.val:
        return searchBST(node.right,target)
    
print(searchBST(A2,4))
