#User function Template for python3

class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        s=""
        l=[]
        d={}
        d[1]=S2
        for i in range(len(S1)):
            s=""
            for j in range(i,len(S1)):
                s+=S1[j]
                if s in d[1]:
                    l.append(s)
                else:
                    break
        # print(l)
        m=0
        for i in l:
            m=max(m,len(i))
        # print(max(l))
        if l==[]:
            return 0
        return m





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n,m = input().strip().split(" ")
        n,m = int(n), int(m)
        S1 = input().strip()
        S2 = input().strip()
        
        
        ob=Solution()
        print(ob.longestCommonSubstr(S1, S2, n, m))
# } Driver Code Ends