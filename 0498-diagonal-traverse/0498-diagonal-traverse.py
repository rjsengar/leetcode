def solve(n,m,mat):
    i=n
    j=0
    l=[]
    while(j<m and i>=0):
        l.append(mat[i][j])
        i-=1
        j+=1
    return l
def solve1(n,m,mat,t):
    i=n
    j=m
    l=[]
    while(j<t and i>=0):
        l.append(mat[i][j])
        i-=1
        j+=1
    return l
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        l1=[]
        n=len(mat)
        m=len(mat[0])
        for i in range(len(mat)):
            k=solve(i,m,mat)
            l1.append(k)
        for i in range(1,m):
            k=solve1(n-1,i,mat,m)
            l1.append(k)
        p=0
        l2=[]
        for i in l1:
            if p%2!=0:
                for j in i[::-1]:
                    l2.append(j)
            else:
                for j in i:
                    l2.append(j)
            p+=1
        return l2

        # print(l1)
        return []
        