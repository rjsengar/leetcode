
class Solution:
    def nthFibonacci(self, n : int) -> int:
        l=[0]*(n+1)
        l[0]=0
        l[1]=1
        for i in range(2,n+1):
            l[i]=(l[i-1]+l[i-2])%1000000007
            # print(l)
        return l[n]
        






#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.nthFibonacci(n)
        
        print(res)
        

# } Driver Code Ends