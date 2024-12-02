#User function Template for python3

class Solution:
    def search(self, pat, txt):
        k=len(pat)
        l=[]
        for i in range(len(txt)-len(pat)+1):
            if txt[i:i+k]==pat:
                l.append(i)
        return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans) == 0:
            print("[]", end="")
        for value in ans:
            print(value, end=' ')
        print()

# } Driver Code Ends