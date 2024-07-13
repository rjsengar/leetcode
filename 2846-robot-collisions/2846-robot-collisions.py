class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        s=[]
        l=[]
        p=positions[:]
        dire={}
        pos={}
        heal={}
        for i in range(len(positions)):
            dire[positions[i]]=directions[i]
            heal[positions[i]]=healths[i]
    
        positions.sort()

        for i in range(len(positions)):
            if s and s[-1][2]=='R' and dire[positions[i]]=='L':
                if s[-1][1]==heal[positions[i]]:
                    s.pop()
                elif s[-1][1]<heal[positions[i]]:
                    while(s and s[-1][1]<heal[positions[i]] and s[-1][2]=='R'):
                        s.pop()
                        heal[positions[i]]-=1
                    if (s and s[-1][1]==heal[positions[i]] and s[-1][2]=='R'):
                        s.pop()
                    elif (s and s[-1][1]>heal[positions[i]] and s[-1][2]=='R'):
                        s[-1][1]-=1
                    else:
                        s.append([positions[i],heal[positions[i]],dire[positions[i]]])
                elif s[-1][1]>heal[positions[i]]:
                    s[-1][1]-=1
            else:
                s.append([positions[i],heal[positions[i]],dire[positions[i]]])
        l1=[]
        d2={}
        for i in s:
            d2[i[0]]=i[1]
        for i in p:
            if i in d2:
                l1.append(d2[i])
        return l1
                
        