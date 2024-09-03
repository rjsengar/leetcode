class Solution:
    def getLucky(self, s: str, k: int) -> int:
        d={}
        l=[]
        m=0
        for i in range(1,27):
            d[chr(96+i)]=i
        s1=""
        for i in s:
            s1+=str(d[i])
        for i in range(k+1):
            m=0
            if(len(l)==1):
                return int(l[0])
            l=list(s1)
            for i in l:
                m+=int(i)
            s1=str(m)
        n="".join(l)
        return int(n)
        


    
        

        
