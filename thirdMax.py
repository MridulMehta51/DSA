class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maximum=float("-inf")
        
        m=0
         # [2,2,3,1]
        nums.sort()
        for i in range(len(nums)-1,-1,-1):
            if m==3:
                return maximum
            if nums[i]==maximum:
                continue
            else:
                maximum=nums[i]
                m+=1
        if m <3:
            return max(nums)
        return maximum
        
        
        
      
