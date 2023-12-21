#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def lemonadeChange(self, N, bills):
        c=0
        c1=0
        for i in bills:
            if i==5:
                c+=1
            elif i==10:
                if c==0:
                    return False
                else:
                    c1+=1
                    c-=1
            elif i==20:
                if (c1>=1 and c>=1):
                    c-=1
                    c1-=1
                elif c>=3:
                    c-=3
                else:
                    return False
        return True



#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        bills = list(map(int, input().split()))
        ob = Solution()
        res = ob.lemonadeChange(N, bills)
        print(res)
# } Driver Code Ends