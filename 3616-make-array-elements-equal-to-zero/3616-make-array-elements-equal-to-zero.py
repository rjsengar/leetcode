class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        if nums.count(0)==0:
            return 0
        l1=nums[:]
        c=0
        for i in range(len(nums)):
            if nums[i]==0:
                j=i+1
                l=0
                r=1
                while(1):
                    if r:
                        t=0
                        while(j<len(nums)):
                            if nums[j]>0:
                                t=1
                                nums[j]-=1
                                l=1
                                r=0
                                j-=1
                                break
                            j+=1
                        if t==0:
                            break
                    else:
                        t=0
                        while(j>=0):
                            if nums[j]>0:
                                t=1
                                nums[j]-=1
                                l=0
                                r=1
                                j+=1
                                break
                            j-=1
                        if t==0:
                            break
                    # print(nums)
                    if not t:
                        break
                if sum(nums)==0:
                    c+=1
                
            nums=l1[:]
        nums=l1[:]
        for i in range(len(nums)):
            if nums[i]==0:
                j=i-1 
                l=1
                r=0
                while(1):
                    if r:
                        t=0
                        while(j<len(nums)):
                            if nums[j]>0:
                                t=1
                                nums[j]-=1
                                l=1
                                r=0
                                j-=1
                                break
                            j+=1
                        if t==0:
                            break
                    else:
                        t=0
                        while(j>=0):
                            if nums[j]>0:
                                t=1
                                nums[j]-=1
                                l=0
                                r=1
                                j+=1
                                break
                            j-=1
                        if t==0:
                            break
                    # print(nums)
                    if  not t:
                        break

                if sum(nums)==0:
                    c+=1
            nums=l1[:]
        return c

        