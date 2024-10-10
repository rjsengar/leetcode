class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        m=0
        st=[]
        for i in range(len(nums)):
            if st==[] or nums[st[-1]]>nums[i]:
                st.append(i)
            else:
                # print(st)
                k=len(st)-1
                while(k>=0 and nums[st[k]]<=nums[i]):
                    m=max(i-st[k],m)
                    k-=1  
        return m
        