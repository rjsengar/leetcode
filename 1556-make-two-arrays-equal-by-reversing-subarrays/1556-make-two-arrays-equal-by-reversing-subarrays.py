class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # for i in range(len(arr)):
        #     for j in range(i,len(arr)+1):
        #         s=arr[i:j]
        #         s=s[::-1]
        #         if arr[:i]+s+arr[j:]==target:
        #             return True
        target.sort()
        arr.sort()
        if target==arr:
            return True
        return False
        