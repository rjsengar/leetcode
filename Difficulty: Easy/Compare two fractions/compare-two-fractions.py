#User function Template for python3


class Solution:
    def compareFrac (self, str):
        s=str.split(', ')
        a=s[0].split('/')
        b=s[1].split('/')
        c1=int(a[0])/int(a[1])
        c2=int(b[0])/int(b[1])
        if c1==c2:
            return'equal'
        elif c1>c2:
            return s[0]
        else:
            return s[1]
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import re

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        str = input()
        print(ob.compareFrac(str))

# } Driver Code Ends