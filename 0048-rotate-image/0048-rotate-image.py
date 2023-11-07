class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l=[]
        m=[]
        for i in range(len(matrix)):
            l=[]
            for j in range(len(matrix[i])):
                l.append(matrix[j][i])
            m.append(l[::-1])
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j]=m[i][j]
        return matrix
        