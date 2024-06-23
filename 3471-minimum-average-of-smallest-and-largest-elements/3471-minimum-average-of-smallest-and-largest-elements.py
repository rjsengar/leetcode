class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        l=[]
        while(nums):
            c=(nums.pop(0)+nums.pop())/2
            l.append(c)
        return min(l)

        