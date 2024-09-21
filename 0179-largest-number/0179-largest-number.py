class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        nums.sort(reverse=True)
        if len(nums)==nums.count('0'):
            return '0'
        for i in range(len(nums)):
            j=i+1
            while(i<len(nums) and j<len(nums)):
                if int(nums[i]+nums[j])<int(nums[j]+nums[i]):
                    nums[i],nums[j]=nums[j],nums[i]
                j+=1
        return "".join(nums)
        # print(nums)
        # i=0
        # l=[nums[0]]
        # l1=[]
        # s=nums[0][0]
        # while(i<len(nums)):
        #     j=i+1
        #     while(j<len(nums) and nums[j][0]==s):
        #         l.append(nums[j])
        #         j+=1
        #     i=j
        #     l1.append(l)
        #     l=[]
        #     if j<len(nums):
        #         s=nums[j][0]
        #         l=[nums[j]]
        # for i in l1:
        #     for j in range(len(i)-1,-1,-1):
        #         k=j-1
        #         while(k>=0 and len(i[k])>=len(i[j]) and i[j]==i[:k] and i[k][len(i[k])+1]>i[k][0])

        # print(l1)

        return ""










        # print(nums)
        # return "".join(nums)
        # l1=[]
        # s=nums[0][0]
        # l=[nums[0]]
        # i=0
        # while(i<len(nums)):
        #     j=i+1
        #     while(j<len(nums) and nums[j][0]==s):
        #         l.append(nums[j])
        #         j+=1
        #     i=j
        #     l1.append(l)
        #     l=[]
        #     if j<len(nums):
        #         s=nums[j][0]
        #         l=[nums[j]]
        # s=""
        # for i in range(len(l1)):
        #     a=list(l1[i])
        #     a.sort(reverse=True)
        #     l1[i]=a
        #     l3=[]
        #     l4=[]
        #     for j in a:
        #         if int(j)%10==0:
        #             l3.append(j)
        #         else:
        #             l4.append(j)
        #     l3="".join(l3)
        #     l4="".join(l4)
        #     s+=l4+l3
        

        # print(l1)
            
            
        # # print(nums)
        # # a=[[1,1,1,3,1,1],[1,1,1,3],[3,0,1]]
        # # a.sort()
        # # print(a)
        # return s