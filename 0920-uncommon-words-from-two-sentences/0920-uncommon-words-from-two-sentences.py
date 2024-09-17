class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d={}
        d1={}
        s1=s1.split()
        s2=s2.split()
        for i in s1:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in s2:
            if i not in d1:
                d1[i]=1
            else:
                d1[i]+=1  
        l=[]
        for i in s1:
            if i not in d1 and d[i]<=1:
                l.append(i)
        for i in s2:
            if i not in d and d1[i]<=1:
                l.append(i)
        
        return l
        