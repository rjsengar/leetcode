class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l2=[]
        for i in nums1:
            if(i in nums2):
                l2.append(i)
                nums2.remove(i)
        return l2