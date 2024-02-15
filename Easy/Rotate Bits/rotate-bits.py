#User function Template for python3

class Solution:
    def rotate(self, N, D):
        arr=[]
        D=D%16
        b=bin(N).replace("0b","")
        l=len(b)
        b='0'*(16-l)+b
        k=b[16-D:]+b[:16-D]
        m=b[D:]+b[:D]
        p=int(k,2)
        q=int(m,2)
        arr.append(q)
        arr.append(p)
        return arr
        





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, d = input().strip().split(" ")
        n, d = int(n), int(d)
        ob = Solution()
        ans = ob.rotate(n, d)
        print(ans[0])
        print(ans[1])
# } Driver Code Ends