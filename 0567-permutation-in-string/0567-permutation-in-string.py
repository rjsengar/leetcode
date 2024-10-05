from itertools import permutations
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        d={}
        l=len(s1)
        i=0
        s1=list(s1)
        s1.sort()
        s1="".join(s1)
        while(i<=len(s2)-l):
            m=s2[i:i+l]
            m=list(m)
            m.sort()
            m="".join(m)
            d[m]=1
            #print(m)
            i+=1
        if s1 in d or s1[::-1] in d:
            return True
        return False
            
        
         