# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        
        left,right=1,n
        
        while left<=right:   
            
            pick=(left+right)//2
            nm=guess(pick)
            
            if nm==0:
                return pick
            elif nm>0:
                left=pick+1
            else:
                right=pick-1
        return -1
        

        
        
    
        
        
