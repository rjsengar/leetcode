class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        s=0
        l,l1=[],[]
        for i in nums:
            s+=i
            l.append(s)
        s=0
        for i in nums[::-1]:
            s+=i
            l1.append(s)
        l1=l1[::-1]
        c=0
        for i in range(len(l)-1):
            if l[i]>=l1[i+1]:
                c+=1
        return c
        