class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        s=0
        c=0
        m=float('inf')
        for i in matrix:
            for j in i:
                if j<0:
                    c+=1
                s+=abs(j)
                m=min(m,abs(j))
        if c%2==0:
            return s
        else:
            return s-(m*2)
        