class Solution:
    def minimumLength(self, s: str) -> int:
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        c=0
        for i in d:
            if d[i]>=3:
                if d[i]%2==0:
                    c+=2
                else:
                    c+=1
            else:
                c+=d[i]
        return c

        