#User function Template for python3
class Solution:

	def rowWithMax1s(self,arr):
	    m=0
	    k=-1
	    for i in range(len(arr)):
	        s=arr[i].count(1)
	        if s>m:
	            m=s
	            k=i
	    return k


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))

        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]

        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends