class Solution:
    def transitionPoint(self, arr, n): 
        if 1 not in arr:
            return -1
        for i in range(n):
            if arr[i]==1:
                return i




#{ 
 # Driver Code Starts
#driver code
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.transitionPoint(arr, n))

# } Driver Code Ends