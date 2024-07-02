
class Solution:
    def oddEven(self, s : str) -> str:
        x=0
        y=0
        d={}
        d1={}
        d2={}
        s1="abcdefghijklmnopqrstuvwxyz"
        for i in range(len(s1)):
            d1[s1[i]]=i+1
            
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in range(len(s)):
            if s[i] not in d2:
                if d[s[i]]%2==0 and d1[s[i]]%2==0:
                    x+=1
                    d2[s[i]]=1
                else:            
                    if d[s[i]]%2!=0 and d1[s[i]]%2!=0:
                        y+=1
                        d2[s[i]]=1
        # print(x+y)
        if (x+y)%2==0:
            return 'EVEN'
        else:
            return "ODD"
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s = (input())

        obj = Solution()
        res = obj.oddEven(s)

        print(res)

# } Driver Code Ends