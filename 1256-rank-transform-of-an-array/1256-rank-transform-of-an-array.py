class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        l=list(set(arr))
        l.sort()
        d={}
        l1=[]
        for i in range(len(l)):
            d[l[i]]=i+1
        for i in arr:
            l1.append(d[i])
        return l1
        
