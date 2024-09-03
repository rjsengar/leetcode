#User function Template for python3
class Solution:
	def minOperations(self, s1, s2):
		nums1=list(s1)
		nums2=list(s2)
        n=len(nums1)
        m=len(nums2)

        prev=[0]*m
        m1=0
        for i in range(n):
            curr=[0]*m
            for j in range(m):
                if nums1[i]==nums2[j]:
                    if j-1<0:
                        curr[j]+=1
                    else:
                        curr[j]=prev[j-1]+1
                else:
                    curr[j]=max(prev[j],curr[j-1])
                
            prev=curr[:]
        m1=max(prev)
        # print(m1)
        k=len(s1)-m1
        g=len(s2)-m1
        
        return k+g

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s1,s2 = input().split()
		ob = Solution()
		ans = ob.minOperations(s1,s2)
		print(ans)
# } Driver Code Ends