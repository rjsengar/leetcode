class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        k=0
        for i in s:
            if k<len(t):
                if i==t[k]:
                    k+=1
        return len(t)-k
        