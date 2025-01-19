class Solution:
   
    def countWays(self, ranges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # Step 1: Sort the ranges
        ranges.sort()
        
        # Step 2: Merge overlapping ranges and count groups
        groups = 0
        prev_end = -1
        
        for start, end in ranges:
            if start > prev_end:
                # New group
                groups += 1
            prev_end = max(prev_end, end)
        
        # Step 3: Compute 2^groups % MOD
        return pow(2, groups, MOD)
