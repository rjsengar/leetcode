class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        for i in s:
            s=s.replace("()","")
        return len(s)
