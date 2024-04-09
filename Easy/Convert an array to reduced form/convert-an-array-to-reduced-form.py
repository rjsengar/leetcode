#User function Template for python3
class Solution:

    def convert(self,arr, n):
        d={}
        l=arr[:]
        l.sort()
        for i in range(n):
            d[l[i]]=i
        for i in range(n):
            arr[i]=d[arr[i]]
           
        
        return arr
            





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.convert(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends