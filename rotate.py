class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        j= (len(nums)-k-1)%len(nums)
        nums[:] = nums[j+1:] +nums[:j+1]
        
