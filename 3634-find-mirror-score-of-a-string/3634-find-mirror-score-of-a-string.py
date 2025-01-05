class Solution:
    def calculateScore(self, s: str) -> int:
        s1="abcdefghijklmnopqrstuvwxyz"
        d={}
        for i in range(len(s1)):
            d[s1[i]]=s1[abs(25-i)]
        d1={} 
        c=0
        for i in range(len(s)):
            if s[i] not in d1:
                d1[s[i]]=[i]
            else:
                d1[s[i]].append(i)
            if  d[s[i]] in d1 and len(d1[d[s[i]]])>=1:
                c+=(i-d1[d[s[i]]].pop())
                d1[s[i]].pop()
        return c
        