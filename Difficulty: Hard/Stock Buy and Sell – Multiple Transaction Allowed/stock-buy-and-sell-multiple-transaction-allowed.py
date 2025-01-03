from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        a=0
        n=len(arr)
        for i in range(1,n):
            if prices[i]>prices[i-1]:
                a+=(prices[i]-prices[i-1])
        return a



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.maximumProfit(arr)
        print(res)

# } Driver Code Ends