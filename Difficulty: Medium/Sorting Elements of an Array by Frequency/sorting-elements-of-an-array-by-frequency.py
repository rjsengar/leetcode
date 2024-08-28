#User function Template for python3
 
class Solution:
   
    #Function to sort the array according to frequency of elements.
    def sortByFreq(self,arr):
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        l=[]
        for i in d:
            l.append([d[i],i])
        l.sort(reverse=True)
        # print(l)
        l1=[]
        l2=[]
        t=l[0][0]
        for i in l:
            if i[0]==t:
                for k in range(t):
                    l2.append(i[1])
            else:
                l1.append(l2[::-1])
                l2=[]
                for k in range(i[0]):
                    l2.append(i[1])
                t=i[0]
                
        if l2:
            l1.append(l2[::-1])
        a=[]
        for i in l1:
            for j in i:
                a.append(j)
        return a
            



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
    for tt in range(t):

        arr = list(map(int, input().strip().split()))
        l = Solution().sortByFreq(arr)
        print(*l)

# } Driver Code Ends