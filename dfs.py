def search(self,target):
        if not self:
            return False
        if self.root==target:
            return True
        
        return (self.left.search(target) if self.left else False )or (self.right.search(target) if self.right else False)
