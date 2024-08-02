class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        i=0
        k=nums.count(1)
        n=len(nums)
        c=0
        t=0
        a=0
        b=0
        i=0
        m=10**5
        j=0
        while(t<n*2):

            if nums[i]==0:
                a+=1
            else:
                b+=1
            c+=1
            if c==k:
                # print(a,b)
                c-=1
                if a>=k-b:
                    m=min(m,a)
                if nums[j]==1:
                    b-=1
                if nums[j]==0:
                    a-=1
                j+=1
                j%=n
            i+=1
            i%=n
            t+=1
        
        if m==100000:
            return 0
        return m

            