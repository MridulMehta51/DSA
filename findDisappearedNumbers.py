class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        m=[]
        i=1
        n=len(nums)
        numi=set(nums)
        while i<=n:
            if i not in numi:
                m.append(i)
            i+=1
        return m
      
