class Solution:
    def sortColors(self, nums: List[int]) -> None:
        c1=0
        c2=0
        c3=0
        for i in range(len(nums)):
            if(nums[i]==0):
                c1+=1
            elif(nums[i]==1):
                c2+=1
            else:
                c3+=1
        k=0
        while(c1!=0):
            nums[k]=0
            k+=1
            c1-=1
        while(c2!=0):
            nums[k]=1
            k+=1
            c2-=1
        while(c3!=0):
            nums[k]=2
            k+=1
            c3-=1
        return nums
        