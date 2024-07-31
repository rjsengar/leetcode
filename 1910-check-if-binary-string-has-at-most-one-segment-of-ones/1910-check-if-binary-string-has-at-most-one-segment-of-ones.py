class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        s1=list(s)
        s1.sort()
        s1="".join(s1)
        s1=s1[::-1]
        if s==s1:
            return True
        return False
        