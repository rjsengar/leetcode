class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l=[]
        for i in range(1,n+1):
            l.append(i)
        i=0
        j=0
        c=0
        while(l):
            if l[i]!=0:
                c+=1
            if c==k:
                if sum(l)-l[i]==0:
                    return l[i]
                l[i]=0
                c=0
            i+=1
            i=i%len(l)

        