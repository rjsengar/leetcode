class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        i=1
        j=1
        while(time):
            i+=j
            if i==1 or i==n:
                j*=-1
            time-=1
        return i
            

        