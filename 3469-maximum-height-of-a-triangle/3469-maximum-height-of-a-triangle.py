class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        k=1
        c1,c2=0,0
        r1,b1=red,blue
        r2,b2=red,blue
        while(1):
            if c1%2==0:
                if (r1-k)>=0:
                    r1-=k
                    c1+=1
                    k+=1
                else:
                    break
            else:
                if (b1-(k))>=0:
                    b1-=k
                    c1+=1
                    k+=1
                else:
                    break
            
        k=1
        while(1):
            if c2%2==0:
                if (b2-k)>=0:
                    b2-=k
                    c2+=1
                    k+=1
                else:
                    break
            else:
                if (r2-(k))>=0:
                    r2-=k
                    c2+=1
                    k+=1
                else:
                    break
        return max(c1,c2)
        