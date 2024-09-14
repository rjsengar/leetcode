class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m=max(nums)
        i=0
        m1=0
        while(i<len(nums)):
            if nums[i]==m:
                j=i+1
                c=1
                while(j<len(nums) and nums[j]==nums[i]):
                    c+=1
                    j+=1
                m1=max(m1,c)
                i=j
            else:
                i+=1
        return m1