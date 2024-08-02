class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        c=0
        while(i<len(prices)-1):
            if prices[i]<prices[i+1]:
                t=prices[i]
                i+=1
                while(i<len(prices)-1 and prices[i]<=prices[i+1]):
                    i+=1
                c+=prices[i]-t
            else:
                i+=1
        return c
        