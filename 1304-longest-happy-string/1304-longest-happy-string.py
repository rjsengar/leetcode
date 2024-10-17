
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        l=[]
        if a:
            l.append([a,'a'])
        if b:
            l.append([b,'b'])
        if c:
            l.append([c,'c'])
        l.sort(reverse=True)
        s=""
        while(1):
            s1=s
            for i in range(len(l)):
                if s=="" or s[-1]!=l[i][1]:
                    if l[i][0]>=2 and i==0:
                        s+=l[i][1]*2
                        l[i][0]-=2
                        break
                    else:
                        if l[i][0]:
                            s+=l[i][1]
                            l[i][0]-=1
                            break
            l.sort(reverse=True)
            # print(l)
            if s==s1:
                break
        return s

        

        
        