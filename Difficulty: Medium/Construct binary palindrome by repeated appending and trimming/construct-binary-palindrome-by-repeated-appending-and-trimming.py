
class Solution:
    def binaryPalindrome(self, n : int, k : int) -> str:
        # code here
        s=['0']*n
        s[0]='1'
        s[-1]='1'
        i=0
        while(i<n):
            s[i]='1'
            i+=k
        j=n-1
        while(j>0):
            s[j]='1'
            j-=k
        return "".join(s)
        
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        k = int(input())

        obj = Solution()
        res = obj.binaryPalindrome(n, k)

        print(res)

# } Driver Code Ends