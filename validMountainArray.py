class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        u=0
        change=0
        d=0
        once=0
        check="up"
        if len(arr)<3:
            return False
        for i in range(1,len(arr)):
            if arr[i-1]<arr[i] and change==0:
                u=1
                check="up"
                once=1
            elif arr[i-1]>arr[i] and once==1:
                change=1
                check="down"
                d=1
            else:
                return False
                
        if  check=="down" and change==1 and once==1:
            return True
                    
                # return True
        return False
