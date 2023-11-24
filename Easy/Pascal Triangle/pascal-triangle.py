#User function Template for python3

#User function Template for python3
class Solution:

	def nthRowOfPascalTriangle(self,n):
	    res=[[1]]
        for i in range(n):
            arr=[0]*(i+1)
            arr[0]=arr[i]=1
            preArr=res[-1]
            for j in range(1,(i//2)+1):
                arr[j]=arr[i-j]=(preArr[j]+preArr[j-1])%(10**9+7)
            res.append(arr)
        return res[n]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

	tc=int(input())
	while tc > 0:
	    n=int(input())
	    ob = Solution()
	    ans=ob.nthRowOfPascalTriangle(n)
	    for x in ans:
	        print(x, end=" ")
	    print()
	    tc=tc-1
# } Driver Code Ends