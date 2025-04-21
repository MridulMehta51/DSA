class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m=""
        k=0
        for i in range(len(s)):
            for j in range(k,len(t)):
                if t[j]==s[i]:
                    m+=t[j]
                    k=j+1
                    break    
        print(m,s)
        return m==s
# Approach-2
        i,j=0,0

        while i<len(s) and j <len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
        return i==len(s)
