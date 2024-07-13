class Solution:
    def validStrings(self, n: int) -> List[str]:
        a=(2**n)
        l=[]
        for i in range(a):
            b=bin(i).replace('0b',"")
            if len(b)<n:
                b='0'+b
            if '00' not in b and len(b)==n:
                l.append(b)
        return l

        