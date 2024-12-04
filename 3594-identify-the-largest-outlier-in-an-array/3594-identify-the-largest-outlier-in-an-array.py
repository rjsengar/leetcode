class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        nums.sort()
        d={}
        # print(nums)
        n=len(nums)
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
        s=sum(nums)
        m=min(nums)
        for i in range(len(nums)):
            s1=s
            s1-=nums[i]
            d[nums[i]]-=1
            if s1%2==0 and (s1//2) in d and d[s1//2]>=1:
                m=max(m,nums[i])
            d[nums[i]]+=1
        return m
            

        return m
                

            
        