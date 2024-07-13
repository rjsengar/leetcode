class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        s=list(s)
        n=len(s)
        l=[]
        for i in range(len(s)):
            l.append(s[(i+k)%n])
        return "".join(l)
        