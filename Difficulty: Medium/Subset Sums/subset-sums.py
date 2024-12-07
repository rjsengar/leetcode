#User function Template for python3
class Solution:
	def subsetSums(self, arr):
	    n=len(arr)
	    l=[]
		def solve(i,s):
		    if i>=n:
		        l.append(s)
		        return
		    solve(i+1,s+arr[i])
		    solve(i+1,s)
		solve(0,0)
		l.sort()
		return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())  # Number of test cases
    for i in range(T):
        arr = [int(x)
               for x in input().split()]  # Reading array for the test case
        ob = Solution()
        ans = ob.subsetSums(arr)  # Getting the subset sums
        ans.sort()  # Sorting the result

        # Printing the subset sums in space-separated format
        for x in ans:
            print(x, end=" ")
        print("")  # Ensuring new line after each test case

# } Driver Code Ends