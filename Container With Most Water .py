class Solution:
    def maxArea(self, height: List[int]) -> int:
        count = 0
        res=0
        i=0
        n=len(height)-1
        j=len(height)-1
        while i<j:
            if height[i]<height[j]:
                count= height[i] * n
                print(height[i],j)
                i+=1  
                n-=1
            else:
                count= height[j] * n
                j-=1
                n-=1
            if res < count:
                res = count
        return res
