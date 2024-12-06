class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        d={}
        for i in banned:
            d[i]=1
        c=0
        s=0
        for i in range(1,min(n,maxSum)+1):
            if i not in d and s+i<=maxSum:
                s+=i
                c+=1
        return c