class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        l1=len(a)
        l2=len(b)
        if a==b:
            return -1
        else:
            if l1>l2:
                return l1
            return l2
        