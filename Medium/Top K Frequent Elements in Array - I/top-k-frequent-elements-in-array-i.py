class Solution:
    def topK(self, nums, k):
        l=[[] for i in range(len(nums) + 1)]
        c={}
        for i in nums:
            c[i] = 1 + c.get(i,0) 
        for i ,c in c.items():
            l[c].append(i)
        res=[]
        l= [sorted(sublist, reverse=True) for sublist in l]

        for i in range(len(l)-1,0,-1):
            for n in l[i]:
               res.append(n)
               if len(res) == k:
                    return res
            
            
            
        
        





#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	a = list(map(int, input().strip().split()))
    	n = a[0]
    	nums = a[1:]
    	k = int(input().strip())
    	obj = Solution()
    	ans = obj.topK(nums, k)
    	for i in ans:
    		print(i, end = " ")
    	print()
    	
# } Driver Code Ends