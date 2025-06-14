from copy import deepcopy
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        
        ans=[1,1]
        
        while rowIndex!=1:
            temp=deepcopy(ans)
            for i in range(1,len(temp)):
                ans[i]=temp[i]+temp[i-1]
                
            ans.append(1)
            rowIndex-=1
            del temp
        return ans
            
