class Solution:
    def numSquares(self, n: int) -> int:
        q=[n]
        t=0
        while(q):
            l=len(q)
            t+=1
            while(l>0):
                n=q[0]
                q.remove(n)
                for j in range(int(n**0.5),0,-1):
                    q.append(n-j*j)
                    if n-(j*j)==0:
                        return t
                l-=1
        