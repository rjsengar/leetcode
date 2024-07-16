class Solution:
    def getSmallestString(self, s: str) -> str:
        s=list(s)
        m=0
        k=-1
        for i in range(len(s)-1):
            a=int(s[i])
            b=int(s[i+1])
            if (a%2==0 and b%2==0) or (a%2!=0 and b%2!=0):
                if a>b:
                    k=i
                    break
        if k==-1:
            return "".join(s)
        else:
            s[k],s[k+1]=s[k+1],s[i]
            return "".join(s)



        