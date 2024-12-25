#User function Template for python3
class Solution:
    def setMatrixZeroes(self, matrix):
        n=len(matrix)
        m=len(matrix[0])
        l=[]
        l1=[]
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    l.append(i)
                    l1.append(j)
        for i in l:
            for p in range(m):
                matrix[i][p]=0
        for j in l1:
            for q in range(n):
                matrix[q][j]=0
        return matrix
                
        


#{ 
 # Driver Code Starts
import sys

# Position this line where user code will be pasted.
if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()

    idx = 0
    t = int(data[idx])
    idx += 1
    results = []

    for _ in range(t):
        n, m = map(int, data[idx:idx + 2])
        idx += 2
        arr = []
        for i in range(n):
            arr.append(list(map(int, data[idx:idx + m])))
            idx += m

        sol = Solution()
        sol.setMatrixZeroes(arr)

        for row in arr:
            results.append(" ".join(map(str, row)))

        results.append("~")

    sys.stdout.write("\n".join(results) + "\n")

# } Driver Code Ends