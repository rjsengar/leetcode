class Solution:
    def modifyString(self, s: str) -> str:
        s1="abcdefghijklmnopqrstuvwxyz"
        d={}
        for i in range(len(s)):
            if s[i]=='?':
                d[i]=1
        s=list(s)
        for i in range(len(s)):
            if s[i]=='?':
                for j in s1:
                    if i-1>=0 and i+1<len(s):
                        if j!=s[i-1] and s[i+1]!=j:
                            s[i]=j
                    elif i-1>=0:
                        if j!=s[i-1]:
                            s[i]=j
                    elif i+1<len(s):
                        if j!=s[i+1]:
                            s[i]=j
                    else:
                        s[i]=j
        return "".join(s)

            
            
