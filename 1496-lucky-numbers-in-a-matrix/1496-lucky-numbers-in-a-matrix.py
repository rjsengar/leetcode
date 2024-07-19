class Solution:
    def luckyNumbers (self, mat: List[List[int]]) -> List[int]:
        l1=[]
        for i in range(len(mat[0])):
            m=0
            for j in range(len(mat)):
                if mat[j][i]>m:
                    k=j
                    m=mat[j][i]
            m1=min(mat[k])
            if m1==m:
                l1.append(m1)

        return l1
                

        