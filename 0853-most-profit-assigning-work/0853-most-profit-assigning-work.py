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
        for i in d:
            l.append([i,d[i]])
        l.sort()
        for i,j in l:
            ma=max(ma,j)
            l1.append([i,ma])
        for i,j in l1:
            d[i]=j
            
        m1=max(worker)+2
        l2=[0]*m1
        ma=0
        for i in range(1,m1):
            if i in d:
                ma=max(ma,d[i])
                l2[i]=ma
            else:
                l2[i]=ma

        for i in worker:
            c+=l2[i]
        return c