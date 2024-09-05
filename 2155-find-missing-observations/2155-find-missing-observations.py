class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        l=[1]*n
        s=sum(l)
        s1=sum(rolls)
        t=len(rolls)+n
        k=(t*mean)-s1
        print(k)
        if k>n*6 or k<n:
            return []
        
        p=0
        while(s<k):
            if l[p]<6:
                l[p]+=1
                s+=1
            else:
                p+=1
            if s==k:
                return l
            p=p%n
        # if (sum(l)+sum(rolls))//t==mean:
        return l
        # return []
                
        # print(k)
        return []
        