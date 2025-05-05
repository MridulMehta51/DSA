class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        count=1
        if num==0:
            return 0
        while num>1:
            if num%2==1:
                num-=1
                # print(num)
                count+=1
            else:
                num=num/2
                count+=1
        return count
        
