#User function Template for python3

class Solution:
    def romanToDecimal(self, S): 
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"C":100,"D":500,"M":1000}
        c=0
        if len(S)==1:
            return d[S[0]]
        for i in range(len(S)):
            if i+1<len(S) and d[S[i]]<d[S[i+1]]:
                c-=d[S[i]]
            else:
                c+=d[S[i]]
        return c




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends