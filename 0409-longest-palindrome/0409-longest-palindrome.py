class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        c=0
        m=0
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d:
            if d[i]%2==0:
                c+=d[i]
            if d[i]%2!=0:
                m=max(m,d[i])
        c+=m
        t=0
        for i in d:
            if d[i]==m:
                t+=1
            if d[i]%2!=0 and (d[i]!=m or t>1):
                c+=d[i]-1
        return c
    

        
        