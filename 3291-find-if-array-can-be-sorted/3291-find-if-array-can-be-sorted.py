class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        i=0
        l=[]
        l1=[]
        for i in nums:
            b=bin(i).replace("0b","")
            a=b.count('1')
            l.append(a)
        i=0
        # print(l)
        while(i<len(nums)-1):
            p=[nums[i]]
            j=i+1
            while(j<len(nums) and l[i]==l[j]):
                p.append(nums[j])
                j+=1
            p.sort()
            for k in p:
                l1.append(k)
            i=j
        # print(l1)
        if len(nums)!=len(l1):
            l1.append(nums[-1])
        nums.sort()
        if l1==nums:
            return True
        return False

            
        