#User function Template for python3
class Solution:
    
    def countBuildings(self,h, n):
        m=0
        c=0
        for i in h:
            if i>m:
                m=i
                c+=1
        return c





#{ 
 # Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        h = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countBuildings(h, n)
        print(ans)
        tc -= 1

# } Driver Code Ends