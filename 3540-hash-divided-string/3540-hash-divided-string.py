class Solution:
    def stringHash(self, s: str, k: int) -> str:
        l=len(s)
        t=l//k
        s1="abcdefghijklmnopqrstuvwxyz"
        d={}
        d1={}
        for i in range(len(s1)):
            d[s1[i]]=i
            d1[i]=s1[i]

        i=0
        l1=[]
        while(i<len(s)):
            l1.append(s[i:i+k])
            i+=k
        s2=""
        for i in l1:
            c=0
            for j in i:
                c+=d[j]
            c=c%26
            s2+=d1[c]
        return s2

        
        