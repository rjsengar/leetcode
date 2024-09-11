class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        c=0
        while(start>0 or goal>0):
            if start%2^goal%2:
                c+=1
            start=start>>1
            goal=goal>>1
        return c


        