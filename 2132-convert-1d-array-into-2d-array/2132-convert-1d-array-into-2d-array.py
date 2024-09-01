class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        l=[]
        p=[]
        for i in range(len(original)):
            l.append(original[i])
            if len(l)==n:
                p.append(l)
                l=[]
        if len(p)!=m or len(l)>0 :
            return []
        return p
                