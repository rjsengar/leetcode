class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s1='abcdefghijklmnopqrstuvwxyz'
        d={}
        for i in range(len(s1)):
            d[s1[i]]=i+1
        c=""
        for i in s:
            c+=str(d[i])
        s2=str(c)
        while(k):
            c=0
            for i in s2:
                c+=int(i)
            k-=1
            s2=str(c)
            if len(s2)==1:
                return c
        return int(s2)


            
        