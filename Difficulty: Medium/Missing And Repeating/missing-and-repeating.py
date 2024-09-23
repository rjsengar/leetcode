#User function Template for python3

class Solution:
    def findTwoElement( self,arr):
        d={}
        l=[]
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d:
            if d[i]==2:
                l.append(i)
        for i in range(1,len(arr)+1):
            if i not in d:
                l.append(i)
                break
        return l
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1

# } Driver Code Ends