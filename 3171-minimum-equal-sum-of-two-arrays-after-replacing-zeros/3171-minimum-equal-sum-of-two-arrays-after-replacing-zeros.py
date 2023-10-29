class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        c1=nums1.count(0)
        c2=nums2.count(0)
        s1=sum(nums1)
        s2=sum(nums2)
        if c1+s1==c2+s2:
            return c1+s1
        if (s1+c1)>=(s2+c2):
            s=s1+c1
            print(s)
            if (s2<s and c2>0 and s-s2>c2) or (s2==s and c2==0):
                return s
            else:
                return -1
        else:
            s=s2+c2
            print(s)
            if (s1<s and c1>0 and s-s1>c1) or (s1==s and c1==0):
                return s
            else:
                return -1
            
        