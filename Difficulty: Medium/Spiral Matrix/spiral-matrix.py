#User function Template for python3

# You are required to complete this fucntion
# Function should return an integer
class Solution:
    def findK(self, a, n, m, k):
        l=[]
        top=0
        bottom=n-1
        left=0
        right=m-1
        while(len(l)<k):
            for i in range(left,right+1):
                l.append(a[top][i])
            top+=1
            for i in range(top,bottom+1):
                l.append(a[i][right])
            right-=1
            for i in range(right,left-1,-1):
                l.append(a[bottom][i])
            bottom-=1
            for i in range(bottom,top-1,-1):
                l.append(a[i][left])
            left+=1
        return l[k-1]



#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[1])]for j in range(n[0])]
        c=0
        for i in range(n[0]):
            for j in range(n[1]):
                matrix[i][j] = arr[c]
                c+=1
        obj = Solution()
        print(obj.findK(matrix, n[0], n[1], n[2]))

# } Driver Code Ends