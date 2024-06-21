class Solution:
    def ExtractNumber(self,sentence):
        s=sentence.split()
        m=-1
        for i in s:
            if i.isdigit() and '9' not in i :
                m=max(m,int(i))
        return m

#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    S = input()
    ob = Solution()
    ans = ob.ExtractNumber(S)
    print(ans)

# } Driver Code Ends