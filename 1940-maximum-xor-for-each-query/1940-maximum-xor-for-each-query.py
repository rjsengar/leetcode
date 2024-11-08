class Solution:
    def getMaximumXor(self, nums: List[int], m: int) -> List[int]:
        s=0
        l=[]
        t=2**m-1
        for i in nums:
            s^=i
            l.append(t^s)
        l=l[::-1]
        return l