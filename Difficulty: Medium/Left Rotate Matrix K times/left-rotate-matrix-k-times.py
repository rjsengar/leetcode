class Solution:
    def rotateMatrix(self, k, mat):
        k=k%len(mat[0])
        l=[]
        for i in mat:
            l.append(i[k:])
        for i in range(len(mat)):
            for j in range(k):
                l[i].append(mat[i][j])
        return l



#{ 
 # Driver Code Starts
import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().strip().split(" "))
        mat = []
        for i in range(n):
            mat.append(list(map(int, input().strip().split(" "))))
        ob = Solution()
        ans = ob.rotateMatrix(k, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end=" ")
            print()

# } Driver Code Ends