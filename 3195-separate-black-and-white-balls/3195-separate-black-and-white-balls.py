class Solution:
    def minimumSteps(self, s: str) -> int:
        c=0
        c1=0
        for i in range(len(s)-1,-1,-1):
            if s[i]=='0':
                c+=1
            if s[i]=='1':
                c1+=c
        return c1


        