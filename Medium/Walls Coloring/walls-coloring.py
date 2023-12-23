#User function Template for python3

class Solution():
    def minCost(self, colors, N):
        pink, black, yellow = 0, 0, 0
        for p, b, y in colors:
            pink, black, yellow = p + min(black, yellow), b + min(pink, yellow), y + min(pink, black)
        return min(pink, black, yellow)  



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ =="__main__":
    for _ in range(int(input())):
        n = int(input())
        colors = []
        for i in range(n):
            tmp = [int(i) for i in input().split()]
            colors.append(tmp)
        print(Solution().minCost(colors, n))
# } Driver Code Ends