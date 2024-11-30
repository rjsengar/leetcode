class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while(1):
            k=1
            s=str(n)
            for i in s:
                k*=int(i)
            if k%t==0:
                return n
            n+=1
        