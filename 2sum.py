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

