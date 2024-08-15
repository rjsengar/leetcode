

class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, nums):
		d={}
		d1={}
		c=0
		nums1=nums[:]
		for i in range(len(nums)):
		    d[nums[i]]=i
		nums1.sort()
		for i in range(len(nums)):
		    d1[nums1[i]]=i
		k=0
		for i in range(len(nums)):
		    if nums[i]!=nums1[i]:
		        x=d[nums1[i]]
		        d[nums[i]]=x
                nums[i],nums[x]=nums[x],nums[i]
                d[nums1[i]]=i
                
                # print(nums)
		      #  print(d)
		      #  print(d1)
		        c+=1
		return c
		        
		


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends