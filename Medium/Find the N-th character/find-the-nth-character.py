#User function Template for python3

class Solution:
    def nthCharacter(self, s, r, n):
        while(r):
            s1=""
            for i in s:
                if i=='1':
                    s1+='10'
                else:
                    s1+='01'
            s=s1[:n+1]
            r-=1
        return s[n]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        snr = input().split()
        S, R, N = snr[0], int(snr[1]), int(snr[2])
        ob = Solution()
        print(ob.nthCharacter(S, R, N))
# } Driver Code Ends