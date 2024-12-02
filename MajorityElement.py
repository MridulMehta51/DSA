# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         freq={}

#         for i in (nums):
#             if i in freq:
#                 freq[i]+=1

#             else:
#                 freq[i]=1


#         maxi=0
#         key=None
#         for i,j in freq.items():
#             if j> maxi:
#                 maxi=j
#                 key=i
                
#         #         # max_key = None
#         # max_value = 0
#         # for key, value in freq.items():
#         #     if value > max_value:
#         #         max_value = value
#         #         max_key = key

#         return key
class Solution:
    def majorityElement(self, nums):
        candidate = 0
        count = 0

        for nums in nums:
            if count == 0:
                candidate = nums
            if nums == candidate:
                count += 1
            else:
                count -= 1

        return candidate
        
