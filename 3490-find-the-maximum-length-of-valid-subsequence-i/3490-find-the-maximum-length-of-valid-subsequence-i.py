class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        c1,c2=0,0
        for i in range(len(nums)):
            if nums[i]%2==0:
                c1+=1
            else:
                c2+=1
        if c1==len(nums) or c2==len(nums):
            return len(nums)
        m=0
        k=0
        c3,c4=0,0
        for i in range(len(nums)):
            if (nums[i])%2==0 and m==0:
                c3+=1
                m=1
            elif nums[i]%2!=0 and m==1:
                c3+=1
                m=0
        m=0
        for i in range(len(nums)):
            if (nums[i])%2!=0 and m==0:
                c4+=1
                m=1
            elif nums[i]%2==0 and m==1:
                c4+=1
                m=0
        return max(c1,c2,c3,c4)

        # return c1
        