class Solution:
    def largestCombination(self, c: List[int]) -> int:
        m=0
        l=[]
        for i in c:
            b=bin(i).replace("0b","")
            m=max(m,len(b))
        l=[0]*m
        for i in c:
            b=bin(i).replace("0b","")
            b=(m-len(b))*'0'+b
            for j in range(len(b)):
                if b[j]=='1':
                    l[j]+=1
        return max(l)
        