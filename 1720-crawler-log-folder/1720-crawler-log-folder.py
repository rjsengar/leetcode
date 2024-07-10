class Solution:
    def minOperations(self, logs: List[str]) -> int:
        c=0
        for i in logs:
            if i=='./':
                continue
            elif i=='x/':
                c+=1
            elif i=='../':
                if c>0:
                    c-=1
            else:
                c+=1
        return c
        