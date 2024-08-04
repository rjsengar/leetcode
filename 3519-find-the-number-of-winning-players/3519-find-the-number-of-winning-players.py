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
                d2={}
                for j in d[i]:
                    if j not in d2:
                        d2[j]=1
                    else:
                        d2[j]+=1
                    if d2[j]>i:
                        c+=1
                        break

        return c
        