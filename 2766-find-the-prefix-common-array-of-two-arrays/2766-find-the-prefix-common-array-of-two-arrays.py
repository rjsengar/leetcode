class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        d=[]
        l=[]
        c=0
        for i in range(len(A)):
            if A[i] in d:
                c+=1
            else:
                d.append(A[i])
            if B[i] in d:
                c+=1
            else:
                d.append(B[i])
            l.append(c)
        return l