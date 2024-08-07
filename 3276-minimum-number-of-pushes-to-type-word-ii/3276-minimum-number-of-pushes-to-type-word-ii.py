class Solution:
    def minimumPushes(self, word: str) -> int:
        d1={}
        c=0
        for i in word:
            if i in "*0#1":
                c+=1
                continue
            if i not in d1:
                d1[i]=1
            else:
                d1[i]+=1

        c1=0
        l=[]
        for i in d1:
            l.append(d1[i])
        l.sort(reverse=True)
        # print(l,d1)
        k=0
        t=1
        for i in l:
            c+=(i*t)
            k+=1
            if k==8:
                t+=1
                k=0
        return c



        