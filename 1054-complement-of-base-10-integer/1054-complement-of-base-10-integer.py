class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b=bin(n).replace('0b',"")
        b=list(b)
        for i in range(len(b)):
            if b[i]=='1':
                b[i]='0'
            else:
                b[i]='1'
        b="".join(b)
        s=int(b,2)
        return s
        