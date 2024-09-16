# User function Template for Python3

class Solution:
    def maxLength(self, s):
        a=[]
        a.append(-1)
        ans=0
        for i in range(len(s)):
            #print(a[-1])
            if s[i]=='(':
                a.append(i)
            else:
                a.pop()
                if len(a)==0:
                    a.append(i)
                ans=max(ans,i-a[-1])
        return ans


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.maxLength(S))

# } Driver Code Ends