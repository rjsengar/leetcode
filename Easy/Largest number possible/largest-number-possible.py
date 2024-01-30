#User function Template for python3

class Solution:
    def findLargest(self, N, S):
        s=""
        if S==0 and N==1:
            return 0
        if S==0 and N>=2:
            return -1
        while(N):
            if S>=9:
                s+='9'
                S-=9
            elif S==0:
                s+='0'
            else:
                s+=str(S)
                S=0
            
            N-=1
        if S!=0:
            return -1
        return int(s)





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, S = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.findLargest(N, S))
# } Driver Code Ends