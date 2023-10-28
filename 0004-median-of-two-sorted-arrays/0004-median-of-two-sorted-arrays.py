class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1=len(nums1)
        l2=len(nums2)
        i=0
        j=0
        l=[]
        while(i<l1 and j<l2):
            if nums1[i]<nums2[j]:
                l.append(nums1[i])
                i+=1
            else:
                l.append(nums2[j])
                j+=1
        while(i<l1):
            l.append(nums1[i])
            i+=1
        while(j<l2):
            l.append(nums2[j])
            j+=1
        l3=len(l)
        
        if l3%2 == 0:
            i1 = l3 / 2  - 1
            i2 = l3/ 2 
            return (l[int(i1)] + l[int(i2)]) / 2
        else:
            idx = (l3 + 1) / 2 - 1
            return l[int(idx)]

