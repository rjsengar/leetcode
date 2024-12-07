class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l1=[]
        n=len(nums)
        def solve(i,s):
            if i>=n:
                # print(s)
                l1.append(s[:])           
                return
            
            s.append(nums[i])
            solve(i+1,s)
            s.pop()
            solve(i+1,s)
        solve(0,[])
        l1.sort()
        return l1