#User function Template for python3

class Solution:
    def pattern (self, arr):
        l1=[]
        l2=[]
        for i in range(len(arr)):
            s1=""
            s2=""
            for j in range(len(arr)):
                s1+=str(arr[i][j])
                s2+=str(arr[j][i])
            l1.append(s1)
            l2.append(s2)
        for i in range(len(l1)):
            a=l1[i]
            if a==a[::-1]:
                return str(i)+" R"
        for i in range(len(l1)):
            b=l2[i]
            if b==b[::-1]:
                return str(i)+" C"

        return "-1"

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        a = list()
        c = 0
        for i in range(0, n):
            X = list()
            for j in range(0, n):
                X.append(arr[c])
                c += 1
            a.append(X)
        ans = ob.pattern(a)
        print(ans)

# } Driver Code Ends