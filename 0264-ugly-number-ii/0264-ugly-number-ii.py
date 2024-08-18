class Solution:
    def nthUglyNumber(self, n: int) -> int:
        d={}
        l=[1]
        d[1]=1
        while(len(l)<n):
            for i in l:
                for j in [2,3,5]:
                    if i*j not in d:
                        d[i*j]=1
                        l.append(i*j)
                if len(l)>=5*n:
                    break
        l.sort()
        return l[n-1]
        