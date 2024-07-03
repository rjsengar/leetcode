class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)<=4:
            return 0
        m=10000000000000
        n=len(nums)-1
        d={}
        nums1=nums[3:]
        nums2=nums[:-3]
        m1=abs(max(nums1)-min(nums1))
        m2=abs(max(nums2)-min(nums2))
        m=min(m,m1,m2)
        # if len(nums)<=5:
        #     for i in range(len(nums)-1):
        #         m=min(m,abs(nums[i]-nums[i+1]))
        #     return m
        for i in range(3):
            m=min(m,abs(nums[i]-nums[n-(3-i)]))
        return m
        