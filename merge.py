class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=0
        j=0
        num = []
        while i < m and j<n:
            if nums1[i]<nums2[j]:
                num.append(nums1[i])
                i+=1
            else:
                num.append(nums2[j])
                j+=1
        while i < m:
            num.append(nums1[i])
            i += 1

        # Append remaining elements from nums2
        while j < n:
            num.append(nums2[j])
            j += 1
        for k in range(len(num)):
            nums1[k]=num[k]
