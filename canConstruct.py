class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        charcount={}


        for i in magazine:
            charcount[i]=charcount.get(i,0)+1

        for i in ransomNote:
            if charcount.get(i,0) ==0:
                return False
            charcount[i]-=1
        return True


        
