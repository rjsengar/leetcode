class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        c=numBottles
        c+=(numBottles//numExchange)
        numBottles=(numBottles//numExchange)+(numBottles%numExchange)
        while(numBottles>=numExchange):
            c+=(numBottles//numExchange)
            numBottles=(numBottles//numExchange)+(numBottles%numExchange)
        return c

        