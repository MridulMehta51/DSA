class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        Approach1
        res=[]
        m=0
        for i in range(len(nums)):
            m+=nums[i]
            res.append(m)
        return res
        Approach2
        for i in range(1,len(nums)):
            nums[i]=nums[i-1]+nums[i]
        return nums


        
