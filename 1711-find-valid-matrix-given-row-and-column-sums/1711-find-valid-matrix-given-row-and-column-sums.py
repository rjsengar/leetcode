class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        l=[]
        for i in range(len(rowSum)):
            l1=[]
            for j in range(len(colSum)):
                l1.append(0)
            l.append(l1)
        for i in range(len(l)):
            l[i][0]=rowSum[i]
        # print(l)
        for j in range(len(l[0])-1):
            s=0
            for k in range(len(l)):
                # print(s)
                if s+l[k][j]>colSum[j]:
                    t=colSum[j]-l[k-1][j]
                    p=l[k][j]
                    l[k][j]=colSum[j]-s
                    l[k][j+1]+=(p-l[k][j])
                    s=colSum[j]
                else:
                    s+=l[k][j]
        return l

        
