class Solution:
    def findComplement(self, num: int) -> int:
        s1=bin(num).replace("0b","")
        s=""
        for i in s1:
            if i=='0':
                s+='1'
            else:
                s+='0'
        d=int(s,2)
        return d