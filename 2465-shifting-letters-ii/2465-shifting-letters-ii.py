class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        l=[0]*len(s)
        d={}
        d1={}
        s1="abcdefghijklmnopqrstuvwxyz"
        for i in range(len(s1)):
            d[s1[i]]=i
            d1[i]=s1[i]
        for i in shifts:
            if i[2]==1:
                l[i[0]]+=1
                if i[1]<len(s)-1:
                    l[i[1]+1]-=1
            else:
                l[i[0]]-=1
                if i[1]<len(s)-1:
                    l[i[1]+1]+=1
        s=list(s)
        su=0
        l1=[]
        for i in l:
            su+=i
            l1.append(su)
        for i in range(len(l1)):
            s[i]=d1[(d[s[i]]+l1[i])%26]
        return "".join(s)

        