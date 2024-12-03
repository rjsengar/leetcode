class Solution:
    def smallestNumber(self, n: int) -> int:
        while(1):
            b=bin(n).replace("0b","")
            if b=='1'*len(b):
                return n
            n+=1
        