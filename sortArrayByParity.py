class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        j=0
        arr=[]
        for i in nums:
            if i%2==0:
                nums[j]=i
                j+=1
            else:
                arr.append(i)
                
        nums=nums[:j]+arr[:]
        return nums
                
        
        
