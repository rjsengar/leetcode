class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        d={}
        d1={}
        l=[]
        p=[]
        for i in range(n):
            p.append(i)
            d[i]=[]
            d1[i]=[]
        for i in invocations:
            d[i[0]].append(i[1])
            d1[i[0]].append(i[1])
            d1[i[1]].append(i[0])

        for i in range(n):
            l.append(0)
        q=[k]
        se={}
        se[k]=1
        while(q):
            t=q[0]
            q.remove(t)
            l[t]=1
            for i in d[t]:
                if i not in se:
                    q.append(i)
                    se[i]=1
        # print(l)
        se={}
        m=[]
        for i in range(n):
            if l[i]==0:
                q=[i]
                m.append(i)
                while(q):
                    t=q[0]
                    q.remove(t)
                    for j in d1[t]:
                        if l[j]==1:
                            return p
                        if j not in se:
                            se[j]=1
                            q.append(j)
                        
        return m
        # return []
            
        

        