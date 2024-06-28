class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        d={}
        l=[]
        for i in range(n):
            d[i]=0
        for i,j in roads:
            d[i]+=1
            d[j]+=1
        for i in d:
            l.append(d[i])
        l.sort()
        c=0
        # print(l)
        for i in range(n):
            c+=(i+1)*(l[i])
        return c

        
        