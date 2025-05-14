class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        m=0
        expected=heights.copy()
        expected.sort()
        for i in range(len(heights)):
            if  heights[i] != expected[i]:
                m+=1
        return m
