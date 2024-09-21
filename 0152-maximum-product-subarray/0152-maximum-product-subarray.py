class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l1=[]
        l=[]
        l2=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                l.append(nums[i])
            elif l and nums[i]==0:
                l1.append(l)
                l=[]
        if l:
            l1.append(l)
        for i in l1:
            c=0
            for j in i:
                if j<0:
                    c+=1
            l2.append(c)
        m=-float('inf')
        if 0 in nums:
            m=0
        else:
            m=min(nums)
        # print(l1,l2)
        for i in range(len(l1)):
            if l2[i]%2==0:
                s=1
                for j in l1[i]:
                    s*=j
                m=max(m,s)
            else:
                s=1
                t=l2[i]
                p=0
                for j in l1[i]:
                    if j<0:
                        t-=1
                    if t==0:
                        break
                    s*=j
                    p+=1
                if p:
                    m=max(m,s)
                t=l2[i]
                s=1
                p=0
                for j in range(len(l1[i])-1,-1,-1):
                    if l1[i][j]<0:
                        t-=1
                    if t==0:
                        break
                    s*=l1[i][j]
                    p+=1
                if p:
                    m=max(m,s)
        return m
                    







