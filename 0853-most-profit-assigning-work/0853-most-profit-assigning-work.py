class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        d={}
        c=0
        for i in range(len(difficulty)):
            if difficulty[i] not in d:
                d[difficulty[i]]=profit[i]
            else:
                d[difficulty[i]]=max(profit[i],d[difficulty[i]])
        l=[]
        ma=0
        l1=[]
        s=difficulty[:]
        s.sort()
        for i in d:
            l.append([i,d[i]])
        l.sort()
        for i,j in l:
            ma=max(ma,j)
            l1.append([i,ma])
        for i,j in l1:
            d[i]=j
        # print(l1)
        m1=max(worker)+2
        l2=[0]*m1
        ma=0
        # print(s)
        # print(d)
        for i in range(1,m1):
            if s and i in d:
                ma=max(ma,d[i])
                l2[i]=ma
            else:
                l2[i]=ma
        # print(l2)

        for i in worker:
            c+=l2[i]
        return c