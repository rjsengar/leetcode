# You are required to complete this method
# Return True/False or 1/0
def isToeplitz(mat):
    m=len(mat)
    n=len(mat[0])
    for i in range(n):
        a=mat[0][i]
        j=i
        k=0
        # print(a)
        while(k<m and j<n):
            if mat[k][j]!=a:
                return 0
            j+=1
            k+=1
    for i in range(m):
        a=mat[i][0]
        j=0
        k=i
        # print(a)
        while(k<m and j<n):
            if mat[k][j]!=a:
                return 0
            j+=1
            k+=1
        
    return 1


#{ 
 # Driver Code Starts
# Your code goes here
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(m)] for j in range(n)]
        k = 0
        for i in range(n):
            for j in range(m):
                matrix[i][j] = arr[k]
                k += 1
        b = isToeplitz(matrix)

        if b == True:
            print("true")
        else:
            print("false")

# } Driver Code Ends