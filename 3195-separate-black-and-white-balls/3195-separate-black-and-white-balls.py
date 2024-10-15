class Solution:
    def minimumSteps(self, s: str) -> int:
        l=list(s)
        c=0
        c1=0
        if sorted(l)==l:
            return 0
        for i in range(len(l)-1,-1,-1):
            if l[i]=='0':
                c+=1
            if l[i]=='1':
                c1+=c
        return c1


        