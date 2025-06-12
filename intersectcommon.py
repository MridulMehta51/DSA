class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
         
        m=list((nums1))
        n=list((nums2))
        md={}
        nd={}
        
        p=[]
        for i in range(len(m)):
            if m[i] in md:
                md[m[i]]+=1
            else:
                md[m[i]]=1
        for i in range(len(n)):
            if n[i] in nd:
                nd[n[i]]+=1
            else:
                nd[n[i]]=1
        print(md)
        print(nd)
        
        for num in md:
            if num in nd:
                common=min(md[num],nd[num])
                p.extend([num]*common)
        return p
        
