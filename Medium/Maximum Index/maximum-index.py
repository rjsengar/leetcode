#User function Template for python3
class Solution:

    def maxIndexDiff(self,arr,n):
        m=0
        c=1
        for i in range(n-1):
            if arr[i]<arr[i+1]:
                c=0
        if c:
            return 0
        for i in range(n):
            j=n-1
            while(i<j):
                if arr[i]<=arr[j]:
                    m=max(m,j-i)
                    break
                else:
                    j-=1
        return m
           
        #code here





#{ 
 # Driver Code Starts
if __name__ == "__main__":
	t = int(input())
	while(t>0):
		num = int(input())
		arr = [int(x) for x in input().strip().split()]
		ob = Solution()
		print(ob.maxIndexDiff(arr,num))
		t-=1
# } Driver Code Ends