class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        nums=letters
        l,r=0,len(letters)
        
        
        if target =="z" or letters[-1]<=target:
            return nums[0]
        while l<=r:
            
            
            m=(l+r)//2
            
            
            if nums[m]<=target:
                l=m+1
            else:
                r=m-1
        return nums[l]
