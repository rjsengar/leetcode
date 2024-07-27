class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l=nums[:]
        l.sort()
        # print(l)
        c=0
        m=0
        m1=0
        for i in range(len(nums)):
            if nums[i]!=l[i]:
                c+=1
                m=max(m,nums[i])
                m1=1
            else:
                if nums[i:]==l[i:]:
                    return c
                elif m1==1:
                    c+=1
        return c

        