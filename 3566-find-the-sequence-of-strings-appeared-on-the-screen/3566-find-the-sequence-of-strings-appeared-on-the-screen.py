class Solution:
    def stringSequence(self, target: str) -> List[str]:
        s1='abcdefghijklmnopqrstuvwxyz'
        s=""
        l=[]
        for i in target:
            p=0
            while(s1[p]!=i):
                l.append(s+s1[p])
                p+=1
            s+=s1[p]
            l.append(s)
        return l


        