class Solution:
    def maximumProfit(self, p):
        sell=p[0]
        buy=p[0]
        profit=0
        n=len(p)
        t,k=0,0
        for i in range(1,n):
            if buy>p[i]:
                buy=p[i]
                t=i
                if t>k:
                    k=t
                    sell=p[t]
            if sell<p[i]:
                sell=p[i]
                k=i
            if sell-buy>profit and t<=k:
                profit=max(profit,sell-buy)
                # print(profit)
            
        return profit
        # code here


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        prices = list(map(int, input().split()))
        # Create a Solution object and calculate the result
        obj = Solution()
        result = obj.maximumProfit(prices)
        # Print the result
        print(result)

# } Driver Code Ends