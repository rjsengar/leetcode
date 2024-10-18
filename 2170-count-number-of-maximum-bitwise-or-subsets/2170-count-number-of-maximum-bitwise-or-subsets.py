class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        s=0
        for i in nums:
            s|=i
        ans=[[]]
        for j in nums:
            ans+=[i+[j] for i in ans]
        c=0
        for i in ans:
            s1=0
            for j in i:
                s1|=j
            if s==s1:
                c+=1
        return c

        