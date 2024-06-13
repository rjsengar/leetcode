#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        n1=n
        s=0
        while(n):
            d=n%10
            s+=(d*d*d)
            n=n//10
        if s==n1:
            return "Yes"
        return "No"


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends