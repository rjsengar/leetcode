#User function Template for python3

class Solution:
    def search(self, pattern, text):
        p=len(pattern)
        t=len(text)
        l=[]
        for i in range(t-(p-1)):
            if text[i:i+p]==pattern:
                l.append(i+1)
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
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends