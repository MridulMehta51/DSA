class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        out=0
        left=0

        for r in range(len(nums)):
            while nums[r]-nums[left] > 2*k:
             
                left+=1
            out=max(out,r-left+1)
               
        return out
