
class Solution:
    def countNumberswith4(self, n : int) -> int:
        l=[]
        for i in range(1,n+1):
            l.append(str(i))
        c=0
        for i in l:
            if '4' in i:
                c+=1
        return c
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.countNumberswith4(n)

        print(res)

# } Driver Code Ends