class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        lii=[]
        for i in range(1,n+1):
            lii.append(i)
        print(lii)
        result=[]
        def back(index,combi):
            if len(combi)==k:
                result.append(combi[:])
                return
         
            for i in range(index,n):
                combi.append(lii[i])
                back(i+1,combi)
                combi.pop()
        back(0,[])
        return result


        
