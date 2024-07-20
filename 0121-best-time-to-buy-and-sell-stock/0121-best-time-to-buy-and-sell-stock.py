class Solution:
    def maxProfit(self, p: List[int]) -> int:
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
        