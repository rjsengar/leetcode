class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a=c**0.5
        a=int(a)
        print(a)
        if c==0:
            return True
        for i in range(1,a+1):
            x=sqrt(c-i*i)
            if x==int(x):
                return True
        return False

        