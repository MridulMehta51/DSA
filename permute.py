class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result=[]
        def back(combi):
            if len(combi)==len(nums):
                result.append(combi[:])
                return
         
            for i in (nums):
                if i not in combi:
                    combi.append(i)
                    back(combi)
                    combi.pop()
        back([])
        return result


        
