class Solution:
    def reverseWords(self, s: str) -> str:
        
        x=s.split()
        # print(x)
        ans=""
        x=x[::-1]
        return " ".join(x)