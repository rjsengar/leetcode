class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        d={}
        for i in range(n):
            d[i]=[]
        for i, j in edges:
            d[j].append(i)
        l=[]
        # print(d)
        for i in d:
            q=[]
            if d[i]==[]:
                l.append([])
            else:
                for j in d[i]:
                    q.append(j)
                l1=[]
                d1={}
                while(q):
                    a=q[0]
                    q.remove(a)
                    l1.append(a)
                    for t in d[a]:
                        if t not in d1:
                            q.append(t)
                            d1[t]=1
                l1=list(set(l1))
                l1.sort()
                l.append(l1)
        return l

        