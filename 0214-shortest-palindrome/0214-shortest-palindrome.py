class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s==s[::-1]:
            return s
        m=""
        for i in range(len(s)-1,-1,-1):
            m+=s[i]
            k=m+s
            if k==k[::-1]:
                return k
        