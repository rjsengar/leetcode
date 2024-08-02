class Solution:
    def minimumDeletions(self, s: str) -> int:
        s=s[::-1]
        m=0
        c=0
        c1,c2=0,0
        i=0
        while(i<len(s)):
            if s[i]=='a':
                c1+=1
                m=1
                i+=1
           
            elif m==1 and s[i]=='b':
                while(i<len(s) and s[i]=='b'):
                    c2+=1
                    i+=1
                # print(c2,c1)
                if c1<=c2:
                    c+=c1
                    c1=0
                    c2=0
                else:
                    c+=c2
                    c1-=c2
                    c2=0
            else:
                i+=1
        return c



      
            
        