class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points=sorted(points, key=lambda x:x[0])
        # print(points)

        ans=[]
        count=0

        for i in points:
            if not ans or ans[-1][1]<i[0]:
                ans.append(i)
                count+=1
            else:
                ans[-1][1]=min(ans[-1][1],i[1])
        print(ans)
        return count
