class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if sum(nums)<x:
            return -1
        if sum(nums)==x:
            return len(nums)
        m=10000000
        l=[]
        l1=[]
        s=0
        t=0
        d1={}
        for i in nums:
            s+=i
            t+=1
            d1[s]=t
            if s>x:
                break
            if s==x:
                m=min(m,t)
            l.append(s)
        s=0
        t=0
        d={}
        for i in range(len(nums)-1,-1,-1):
            s+=nums[i]
            t+=1
            d[s]=t
            if s==x:
                m=min(m,t)
            if s>x:
                break
            l1.append(s)
        p=0
        for i in range(len(l)):
            p+=1
            if x-l[i] in d:
                m=min(m,p+d[x-l[i]])
        if m==10000000:
            return -1
        return m

        