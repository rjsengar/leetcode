#User function Template for python3

class Solution:
    def modify(self, N):
        s=str(N)
        s1=s[0]
        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                s1+=s[i]
        return int(s1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        num = int(input())

        solObj = Solution()

        print(solObj.modify(num))
# } Driver Code Ends