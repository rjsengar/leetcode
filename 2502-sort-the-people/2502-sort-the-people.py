class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d={}
        for i in range(len(names)):
            d[heights[i]]=names[i]
        l=list(d.keys())
        l.sort(reverse=True)
        l1=[]
        for i in l:
            l1.append(d[i])
        return l1