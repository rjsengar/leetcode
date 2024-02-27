#User function Template for python3

class Solution:
    def game_with_number (self, arr,  n) : 
        l=[]
        for i in range(n-1):
            a=arr[i]|arr[i+1]
            l.append(a)
        for i in range(n-1):
            arr[i]=l[i]
        return arr





#{ 
 # Driver Code Starts

#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    res = ob.game_with_number(arr, n);
    print(*res)




# } Driver Code Ends