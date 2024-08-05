class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d={}
        l=[]
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if d[i]==1:
                l.append(i)
        if len(l)<k:
            return ""
        return l[k-1]