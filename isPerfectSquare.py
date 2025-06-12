class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r=0,num//2
        if num==1:
            return True
        while l<=r:
            m=(l+r)//2
            sq=m*m            
            if num==sq:
                return True
            elif sq<num:
                l=m+1
            else:
                r=m-1
        return False
        
