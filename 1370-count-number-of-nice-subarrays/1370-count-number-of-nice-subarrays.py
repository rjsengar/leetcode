class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l=[]
        n=len(nums)
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        s=0
        i=0
        j=0
        c=0
        c1,c2=0,0
        while(i<n):
            s+=nums[i]
            while(s>k and j<=i):
                s-=nums[j]
                j+=1
            if s<=k:
                c1+=i-j+1
            i+=1
        i=0
        j=0
        s=0
        while(i<n):
            s+=nums[i]
            while(s>=k and j<=i):
                s-=nums[j]
                j+=1
            if s<k:
                c2+=(i-j+1)
            i+=1
        return c1-c2
        