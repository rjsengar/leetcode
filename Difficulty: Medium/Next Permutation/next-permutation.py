#User function Template for python3

class Solution:
    def nextPermutation(self, arr):
        # return []
        l=arr[:]
        l.sort(reverse=True)
        if l==arr:
            l.sort()
            for i in range(len(l)):
                arr[i]=l[i]
            return arr
            
        i=len(arr)-1
        m=0
        while(i>=m):
            j=i
            while(j>=m):
                if arr[i]>arr[j]:
                    m=max(m,j)
                    break
                j-=1
            i-=1
        # print(m)
        i=len(arr)-1
        while(i>=0):
            if arr[i]>arr[m]:
                arr[i],arr[m]=arr[m],arr[i]
                s=arr[m+1:]
                s.sort()
                l=arr[:m+1]+s
                break
            i-=1
        # print(l)
        for i in range(len(arr)):
            arr[i]=l[i]
        return arr
        
            
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for i in range(N):
            arr[i] = int(arr[i])

        ob = Solution()
        ob.nextPermutation(arr)
        for i in range(N):
            print(arr[i], end=" ")
        print()

# } Driver Code Ends