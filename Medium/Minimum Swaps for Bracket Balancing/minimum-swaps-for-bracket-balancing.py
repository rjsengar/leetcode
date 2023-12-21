#User function Template for python3
import math
class Solution:
    def minimumNumberOfSwaps(self,s):
        c=0
        m=0
        for i in s:
            if i=='[':
                c-=1
            else:
                c+=1
                if c>0:
                    m+=c
        return m




#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())
        ob = Solution()
        print(ob.minimumNumberOfSwaps(S))
# } Driver Code Ends