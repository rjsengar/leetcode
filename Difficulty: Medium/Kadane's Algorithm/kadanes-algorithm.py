#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        maxSum = arr[0]
        N=len(arr)
        currSum = 0
        for i in range(0, N):
            currSum += arr[i]
            maxSum = max([maxSum, currSum])
            if currSum < 0:
                currSum = 0;
            
        return maxSum

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends