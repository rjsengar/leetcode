class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        A=[]
        A=words
        s = list(A[0])
        for i in A:
            l = []
            for c in i:
                if c in s:
                    l.append(c)
                    s.remove(c)
            s = l
        
        return s
                