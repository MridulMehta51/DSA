class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newarr=set(nums)
        print(newarr)
        latest=sorted(list(newarr))
        if len(nums)==0:
            return 0
        count=1
        maxcount=0
        newlist=[]
        
        for i in range(1,len(latest)):
            if latest[i]-latest[i-1]==1:
                count+=1
            else:
                maxcount=max(maxcount,count)
                count=1       
        return max(maxcount,count)
