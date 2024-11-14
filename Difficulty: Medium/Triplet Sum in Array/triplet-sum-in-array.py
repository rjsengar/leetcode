#User function Template for python3
class Solution:
     
    # Should return true if there exists a triplet in the
    # array arr[] which sums to x. Otherwise false
    def find3Numbers(self, arr, n, x):
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        for i in range(n):
            for j in range(i+1,n):
                if x-(arr[i]+arr[j]) in d:
                    if x-(arr[i]+arr[j])==arr[i] and x-(arr[i]+arr[j])==arr[j]:
                        if d[arr[i]]>=3:
                            return 1
                    elif x-(arr[i]+arr[j])==arr[i]:
                        if d[arr[i]]>=2:
                            return 1
                    elif x-(arr[i]+arr[j])==arr[j]:
                        if d[arr[j]]>=2:
                            return 1
                    else:
                        return 1
        return 0
                        
                        
                    
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, X = map(int, input().strip().split())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        if (ob.find3Numbers(A, n, X)):
            print(1)
        else:
            print(0)
        print("~")

# } Driver Code Ends