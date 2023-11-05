class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i in range(len(nums)):
            if target==nums[i]:
                l.append(i)
                break
        for i in range(len(nums)-1,-1,-1):
            if target==nums[i]:
                l.append(i)
                break
        if target not in nums:
            return [-1,-1]
        return l
        