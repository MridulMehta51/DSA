class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        j=len(nums)-1
        count=0
        while i <=j:
            if nums[i]==val:
                nums[i],nums[j]=nums[j],nums[i]
                count+=1
                j-=1

            else:
                i+=1
        # nums = nums[:len(nums) - count] 
        nums=nums[:len(nums)-count]
        return len(nums)
        # print(nums,"hjbv")
