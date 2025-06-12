class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        m=list(set(nums1))
        n=list(set(nums2))
        md={}
        
        p=[]
        for i in range(len(m)):
            if m[i] in md:
                continue
            else:
                md[m[i]]=1
        for i in range(len(n)):
            if n[i] in md:
                p.append(n[i])
            else:
                continue
        return p
                
            
            
            
        
            
        
