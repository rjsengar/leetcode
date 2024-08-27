class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n=len(nums1)
        m=len(nums2)
        

        prev=[0]*m
        m1=0
        for i in range(n):
            curr=[0]*m
            for j in range(m):
                if nums1[i]==nums2[j]:
                    if j-1<0:
                        curr[j]+=1
                    else:
                        curr[j]=prev[j-1]+1
                    m1=max(m1,curr[j])
                
                    # curr[j]=max(prev[j],curr[j-1])
            prev=curr[:]
        return m1
        