class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        a= nums.sort()
        i=len(nums)-1
        count=0
        res=0
        for i in range(len(nums)):
            if nums[i]== target:
                count+=1
                break
            elif res > target:
                res=0
                i+=1
            else:
                res+=nums[i]
        return count
