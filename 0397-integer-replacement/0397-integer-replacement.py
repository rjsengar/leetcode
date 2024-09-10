class Solution:
    def integerReplacement(self, n: int) -> int:
        c=0
        def solve(n):
            nonlocal c
            if n<=1:
                return 0
            if n%2==0:
                return 1+solve(n//2)
            else:
                a=1+solve(n-1)
                b=1+solve(n+1)
                return min(a,b)
            
        a=solve(n)
        return a

        