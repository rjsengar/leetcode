class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        f=0
        for i in s:
            if i=='0':
                f=1
            elif f==1 and i=='1':
                return False
        return True
        