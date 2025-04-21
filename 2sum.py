
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_to_index = {} 
        for i in range(len(numbers)):
            num = numbers[i]
            com = target - num 
            if com in num_to_index:
                return [num_to_index[com] + 1, i + 1]
            num_to_index[num] = i 
        return []

# Approach 2 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j] == target:
                    return [i+1,j+1]
        return -1

        
# Approach 3 
        left,right=0,len(numbers)-1

        while left<right:
            current=numbers[left]+numbers[right]

            if current==target:
                return[left+1,right+1]
            elif current > target:
                right-=1
            else:
                left+=1
        return -1
