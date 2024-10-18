class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        s=0
        for i in nums:
            s|=i
        ans=[[]]
        for j in nums:
            l1=[]
            for i in ans:
                a = i+[j]
                l1.append(a)
            for k in l1:
                ans.append(k)
        c=0
        for i in ans:
            s1=0
            for j in i:
                s1|=j
            if s==s1:
                c+=1
        return c

        