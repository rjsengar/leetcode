class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        c=0
        d={}
        c2=0
        maximumHeight.sort(reverse=True)
        for i in maximumHeight:
            if i not in d:
                d[i]=1
                c+=i
                c2=i
            else:
                m=c2-1
                if m<=0:
                    return -1
                else:
                    d[m]=1
                    c2=m
                    c+=m
        return c


            
        