#User function Template for python3

class Solution:
    def findK(self, a, n, m, k):
        matrix=a
        left, right, top, bottom = 0, len(matrix[0])-1, 0, len(matrix)-1
        res = []

        while left<=right and top<=bottom:

            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1

            if left>right or top>bottom:
                break
            
            for i in range(right, left-1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1

            for i in range(bottom, top-1, -1):
                res.append(matrix[i][left])
            left += 1
        return res[k-1]





#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n, m, k = map(int,input().split())
    a = [
            list(map(int,input().split()))
            for _ in range(n)
        ]
    
    ob = Solution()
    print(ob.findK(a,n,m,k))
    
# } Driver Code Ends