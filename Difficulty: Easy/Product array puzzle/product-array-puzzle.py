#User function Template for python3

class Solution:
    def productExceptSelf(self, nums):
        if nums.count(0)>=2:
            return [0]*len(nums)
        s=1
        l=[]
        if 0 in nums:
            for i in nums:
                if i==0:
                    continue
                s*=i
            for i in range(len(nums)):
                if nums[i]==0:
                    l.append(s)
                else:
                    l.append(0)
            return l
        else:
            for i in nums:
                s*=i
            for i in range(len(nums)):
                l.append(s//nums[i])
            return l
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)

# } Driver Code Ends