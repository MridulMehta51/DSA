class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        maxi=-1
        # [17,18,5,4,6,1]
        for i in range(len(arr)-1,-1,-1):
            original=arr[i]
            arr[i]=maxi
            maxi=max(maxi,original)
        return arr
        
