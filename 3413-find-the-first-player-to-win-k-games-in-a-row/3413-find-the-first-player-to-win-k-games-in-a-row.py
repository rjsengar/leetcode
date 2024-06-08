class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        d={}
        d1={}
        for i in range(len(skills)):
            d[skills[i]]=i
            d1[skills[i]]=0
        i=0
        m=max(skills)
        if k>=len(skills):
            return d[m]
        while(1):
            if skills[0]==m:
                return d[skills[0]]
            a=skills[0]
            b=skills[1]
            if a>b:
                d1[a]+=1
                if d1[a]==k:
                    return d[a]
                d1[b]=0
                skills.pop(1)
                skills.append(b)
            else:
                d1[b]+=1
                if d1[b]==k:
                    return d[b]
                d1[a]=0
                skills.pop(0)
                skills.append(a)

        