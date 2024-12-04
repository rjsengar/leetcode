class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        l1=list(str1)
        l2=list(str2)
        c=0
        d={}
        d1={}
        k=len(l1)-1
        s1='abcdefghijklmnopqrstuvwxyz'
        for i in range(len(s1)):
            d[s1[i]]=i
            d1[i]=s1[i]
        i=len(l2)-1
        while(i>=0 and k>=0):
            if l2[i]==l1[k]:
                c+=1
                i-=1
                k-=1
                continue
            elif d1[(d[l1[k]]+1)%26]==l2[i]:
                c+=1
                i-=1
            k-=1
        if c==len(l2):
            return True
        return False
        
        