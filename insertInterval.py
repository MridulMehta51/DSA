class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals=sorted(intervals,key = lambda x:x[0])
        print(intervals)
        ans=[]
        for i in intervals:
            if not ans or ans[-1][1]<i[0]:
                ans.append(i)
            else:
                ans[-1][1]=max(ans[-1][1],i[1])

        return ans

        
