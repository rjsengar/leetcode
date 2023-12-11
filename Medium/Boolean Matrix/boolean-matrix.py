#User function Template for python3


#Function to modify the matrix such that if a matrix cell matrix[i][j]
#is 1 then all the cells in its ith row and jth column will become 1.
def booleanMatrix(matrix):
    d={}
    d1={}
    l=len(matrix)
    l1=len(matrix[0])
    for i in range(len(matrix)):
        if 1 in matrix[i]:
            d[i]=1
            
    for i in range(l):
        for j in range(l1):
            if matrix[i][j]==1:
                d1[j]=1
    
    for i in range(l):
        for j in range(l1):
            if i in d:
                matrix[i][j]=1
    
    for i in range(l):
        for j in range(l1):
            if j in d1:
                matrix[i][j]=1
    
    
    #print(d)
    #print(d1)
    return matrix
                    
        





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        booleanMatrix(matrix)
        for i in range(r):
            for j in range(c):
                print(matrix[i][j], end=' ')
            print()


# } Driver Code Ends