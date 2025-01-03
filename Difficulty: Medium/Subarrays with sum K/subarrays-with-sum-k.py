#User function Template for python3

class Solution:
    def countSubarrays(self, arr, k):
        l=[]
        s=0
        d={}
        d[0]=1
        c=0
        for i in arr:
            s+=i
            if s not in d:
                d[s]=1
            else:
                d[s]+=1
            if (s-k) in d:
                c+=d[s-k]
        return c
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.countSubarrays(arr, k)
        print(res)
        print("~")

# } Driver Code Ends