#User function Template for python3
class Solution:
	def longSubarrWthSumDivByK (self,arr,  n, K) : 
	    pre=[0]*(n+1)
        for i in range(n):
            pre[i+1]=(arr[i]+pre[i])%K
        d={}
        ans=0;
        for i in range(n+1):
            if(pre[i] not in d):
                d[pre[i]]=i
            else:
                ans=max(ans,i-d[pre[i]])
        return ans
		            




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	for _ in range(0,int(input())):
		n, K = map(int ,input().split())
		arr = list(map(int,input().strip().split()))
		ob = Solution()
		res = ob.longSubarrWthSumDivByK(arr, n, K)
		print(res)




# } Driver Code Ends