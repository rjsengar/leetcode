class Solution:
    def distinctIntegers(self, n: int) -> int:
        c=0
        d={}
        if n==1:
            return 1
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i%j==1 and i not in d:
                    d[i]=1
                    c+=1
        return c
        