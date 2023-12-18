#User function Template for python3

class Solution:
    def is_bleak(self, n):
        return 0 if any(i+bin(i).count("1")==n for i in range(n-30,n)) else 1





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.is_bleak(n)
		print(ans)

# } Driver Code Ends