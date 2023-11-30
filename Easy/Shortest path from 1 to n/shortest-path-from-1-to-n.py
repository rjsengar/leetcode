#User function Template for python3

class Solution:
    def minimumStep (self, n):
        c=0
        while(n>0):
            if n%3==0:
                n/=3
                c+=1
            else:
                c+=1
                n-=1
        return c-1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        ob = Solution()
        print(ob.minimumStep(n))
# } Driver Code Ends