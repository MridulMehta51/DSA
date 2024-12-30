class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # Create an empty hashmap to store the most recent index of each number
        hashmap = {}

        # Iterate through the array
        for i, num in enumerate(nums):
            if num in hashmap:
                # Check if the current index and the previous index of the same number are within k distance
                if i - hashmap[num] <= k:
                    return True
            
            # Update the hashmap with the most recent index of the number
            hashmap[num] = i
        
        # No such pair found
        return False
