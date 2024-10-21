class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        i=0
        j=0
        c=0
        n=len(s)
        while(i<n):
            j=i
            d={}
            while(j<n):
                if s[j] not in d:
                    d[s[j]]=1
                else:
                    d[s[j]]+=1
                if d[s[j]]==k:
                    c+=(n-j)
                    break
                j+=1
            i+=1
        return c
        