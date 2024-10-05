class Solution:
    def kthCharacter(self, k: int) -> str:
        s='a'
        s1='abcdefghijklmnopqrstuvwxyz'
        d={}
        d1={}
        for i in range(len(s1)):
            d[s1[i]]=i+1
            d1[i+1]=s1[i]
        t=0
        while(len(s)<k):
            s1=s
            for i in s1:
                s+=d1[(d[i]+1)%26]
        return s[k-1]

            



        