#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def modifyAndRearrangeArr (self, arr) :
        l=[]
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                arr[i]=arr[i]*2
                arr[i+1]=0
        for i in arr:
            if i:
                l.append(i)
        for i in range(len(arr)-len(l)):
            l.append(0)
        return l
            


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.modifyAndRearrangeArr(arr)
        print(*ans)
        print("~")
        t -= 1


# } Driver Code Ends