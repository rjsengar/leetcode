class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m=-100000
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            if(s>m):
                m=s
            if(s<0):
                s=0
        return m
