#User function Template for python3
from queue import PriorityQueue
class Solution:
    #Function to return the minimum cost of connecting the ropes.
   def minCost(self, arr):
    
        # code here
        q=PriorityQueue()
        arr.sort()
        for i in arr:
            q.put(i)
        c=0
        while(q.qsize()>1):
            a=q.get()
            b=q.get()
            k=a+b
            q.put(k)
            c+=k
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
import heapq
from collections import defaultdict
# Contributed by : Nagendra Jha

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
        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.minCost(a))

# } Driver Code Ends