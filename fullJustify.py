class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res=[]
        line=[]
        length=0
        i=0
        
        while i<len(words):
            if length + len(line)+len(words[i]) >maxWidth:
                extra_space = maxWidth-length
                spaces=extra_space//max(1,len(line)-1)
                rem=extra_space % max(1,len(line)-1)
                
                for j in range(max(1,len(line)-1)):
                    line[j]+= " "*spaces
                    if rem:
                        line[j]+=" "
                        rem-=1
                res.append("".join(line))
                line,length=[],0

            line.append(words[i])
            length+=len(words[i])
            i+=1
        last=" ".join(line)
        trail=maxWidth-len(last)
        res.append(last+ " " *trail)
        return res
