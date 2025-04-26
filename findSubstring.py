class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len=len(words[0])
        count=len(words)
        total_words=count*word_len

        word_count={}
        result=[]

        for word in words:
            if word in word_count:
                word_count[word]+=1
            else:
                word_count[word]=1

        for i in range((word_len)):
            left=i
            sub_count={}
            count=0
            for j in range(i,len(s)-word_len +1, word_len):
                sub_word= s[j:j+word_len]

                if sub_word in word_count:
                    if sub_word in sub_count:
                        sub_count[sub_word]+=1
                    else:
                        sub_count[sub_word]=1
                    count+=1

                    while sub_count[sub_word]> word_count[sub_word]:
                        sub_count[s[left:left+word_len]]-=1
                        count-=1
                        left+=word_len

                    if count ==len(words):
                        result.append(left)
                else:
                    sub_count.clear()
                    count=0
                    left=j+word_len
        return result

