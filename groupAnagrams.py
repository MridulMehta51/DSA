from collections import defaultdict;
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams =  defaultdict(list)

        for i in strs:
            count= [0]*26
            for j in i:
                count[ord(j)-ord('a')]+=1
            anagrams[tuple(count)].append(i)
        return list(anagrams.values()) 
