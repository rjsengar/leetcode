class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        d={}
        for i in range(n):
            d[i]=1
        for i in edges:
            a=i[0]
            b=i[1]
            d[b]-=1
        m=-1000000
        k=-1
        for i in d:
            if d[i]==m:
                return -1
            if d[i]>m and d[i]>0:
                m=d[i]
                k=i
        return k
