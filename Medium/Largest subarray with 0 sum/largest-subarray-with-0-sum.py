#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        m=0
        i=-1
        j=0
        d={}
        d[j]=i
        while i<n-1:
            i+=1
            j+=arr[i]
            if j not in d:
                d[j]=i
            else:
                size=i-d[j]
                if size>m:
                    m=size
        return m





#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends