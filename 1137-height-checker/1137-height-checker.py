class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        l=[]
        c=0
        for i in heights:
            l.append(i)
        l.sort()
        for i in range(len(heights)):
            if l[i]!=heights[i]:
                c+=1
        return c