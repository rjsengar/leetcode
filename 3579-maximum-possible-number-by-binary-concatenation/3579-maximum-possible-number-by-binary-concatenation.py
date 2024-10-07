class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        b1=bin(nums[0]).replace("0b","")
        b2=bin(nums[1]).replace("0b","")
        b3=bin(nums[2]).replace("0b","")
        return max(int(b1+b2+b3,2),int(b1+b3+b2,2),int(b2+b1+b3,2),int(b2+b3+b1,2),int(b3+b1+b2,2),int(b3+b2+b1,2))

        