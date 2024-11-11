class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        m=max(nums)
        # nums.sort()
        l=[]
        def SieveOfEratosthenes(num):
            prime = [True for i in range(num+1)]
            p = 2
            while (p * p <= num):
                if (prime[p] == True):
                    for i in range(p * p, num+1, p):
                        prime[i] = False
                p += 1
            for p in range(2, num+1):
                if prime[p]:
                    l.append(p)
        SieveOfEratosthenes(m)
        # print(l)
        for i in range(len(nums)-2,-1,-1):
            if nums[i]>=nums[i+1]:
                a=0
                for j in l:
                    if j<nums[i] and (nums[i]-j)<nums[i+1]:
                        a=j
                        break
                if a==0:
                    return False
                nums[i]=nums[i]-a
        n1=nums[:]
        # print(n1)
        n1.sort()
        if len(nums)==len(list(set(nums))) and n1==nums :
            return True
        return False

        
        