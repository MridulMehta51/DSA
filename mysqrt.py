class Solution:
    def mySqrt(self, x: int) -> int:
    
        left,right=1,x
        
        
        while left<=right:
            
            m=(left+right)//2
            
            square=m*m
            
            if x==square:
                return m
            
            elif square<x:
                left=m+1
                
            else:
                right=m-1
                
        return right
                
        
        
