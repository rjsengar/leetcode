def mat(n,m,arr):
    c=0
    k=n
    d={}
    for i in range(n,n+3):
        for j in range(m,m+3):
            if arr[i][j] in d or arr[i][j]>9 or arr[i][j]<=0:
                return False
            else:
                d[arr[i][j]]=1
    # print(n,m)
    for i in range(m,m+3):
        c=0
        c4=0
        for t in range(m,m+3):
            c4+=arr[k][t]
            
        for j in range(n,n+3):
            c+=arr[j][i]
        
        if c!=c4:
            return False
        k+=1
    # print(c4,c,'a')
    c1=0
    c2=0
    i=n
    j=m
    while(i<n+3 and j<m+3):
        c1+=arr[i][j]
        i+=1
        j+=1
    # print(c1,c)
    if c1!=c:
        return False
    i=n
    j=m+2
    while(j>=m and i!=n+3):
        c2+=arr[i][j]
        i+=1
        j-=1
    # print(c1,c2,'b')
    if c2!=c:
        return False
    
    
    return True

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        c=0
        for i in range(n-2):
            for j in range(m-2):
                # print(i,j)
                if mat(i,j,grid):
                    c+=1
        return c

        