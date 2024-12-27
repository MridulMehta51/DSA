class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split(" ")
        if len(pattern)!=len(words):
            return False
        chartoword={}
        wordtochar={}
        
        for i,j in zip(pattern,words):
            if i in chartoword and chartoword[i]!=j:
                return False
            if j in wordtochar and wordtochar[j]!=i:
                return False
            chartoword[i]=j
            wordtochar[j]=i
        return True

        
