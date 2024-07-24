class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        count=0
        n= len(s)

        while n >0 and s[n-1] == " ":   
            n-=1
        for i in range(n-1,-1,-1):
            if s[i] == " ":
                break
            else:
                count+=1
        return count

        
