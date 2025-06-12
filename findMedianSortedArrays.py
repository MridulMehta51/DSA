class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums1.extend(nums2)
        
        nums1.sort()
        print(nums1)
        
        n=len(nums1)
        print(n)
        m=n//2
        if n%2==1:
            return float(nums1[m])
        else:
            return float((nums1[m]+nums1[m-1])/2)
        
