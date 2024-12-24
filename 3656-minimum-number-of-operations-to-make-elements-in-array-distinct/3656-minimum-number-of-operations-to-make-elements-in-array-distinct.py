class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(list(set(nums)))==len(nums):
            return 0
        c=0
        while(len(nums)>2):
            nums.pop(0)
            nums.pop(0)
            nums.pop(0)
            c+=1
            if len(list(set(nums)))==len(nums):
                return c
        if nums and len(list(set(nums)))!=len(nums):
            return c+1
        return c