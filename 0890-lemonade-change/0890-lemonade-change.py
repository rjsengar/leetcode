class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        a=[5,10,20]
        d={}
        for i in a:
            d[i]=0
        for i in bills:
            if i==5:
                d[i]+=1
            elif i==10:
                d[i]+=1
                if d[5]:
                    d[5]-=1
                else:
                    return False
            elif i==20:
                if d[10] and d[5]:
                    d[10]-=1
                    d[5]-=1
                elif d[5]>=3:
                    d[5]-=3
                else:
                    return False
        return True
                
        