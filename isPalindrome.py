class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        m=str(x)
        i,j=0,len(m)-1
        for i in range(len(m)//2):
            if m[i]!=m[len(m)-i-1]:
                return False
            
        return True


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        m=str(x)
        i,j=0,len(m)-1
        while i<j:
            if m[i]!=m[j]:
                return False
            i+=1
            j-=1
            
        return True
        
