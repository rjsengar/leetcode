class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        d={}
        for i in range(n):
            d[i]=[]
        c=0
        for i in pick:
            d[i[0]].append(i[1])
        for i in d:
            if i==0:
                if d[i]:
                    c+=1
            else:
                s=list(set(d[i]))
                for j in s:
                    if d[i].count(j)>i:
                        c+=1
                        break

        return c
        