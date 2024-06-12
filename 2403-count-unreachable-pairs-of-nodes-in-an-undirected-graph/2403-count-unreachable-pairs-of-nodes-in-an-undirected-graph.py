class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        d={}
        d1={}
        for i in range(n):
            d[i]=0
            d1[i]=[i]
        for i,j in edges:
            d1[i].append(j)
            d1[j].append(i)
        c=0
        l=[]
        l1=[]
        for i in range(n):
            q=[i]
            l1=[]
            while(q):
                n=q[0]
                q.remove(n)
                for k in d1[n]:
                    if d[k]==0:
                        q.append(k)
                        l1.append(k)
                        d[k]=1
            if l1:
                l.append(len(l1))
        if len(l)==1:
            return 0
        s=[]
        s1=0
        # print(l)
        l=l[::-1]
        for i in l:
            s1+=i
            s.append(s1)
        s=s[::-1]
        l=l[::-1]
        # print(s)
        for i in range(len(s)-1):
            c+=l[i]*s[i+1]
        return c
