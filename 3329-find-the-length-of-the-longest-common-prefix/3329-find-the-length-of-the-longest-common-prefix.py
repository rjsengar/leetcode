class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        m=0
        d={}
        for i in range(len(arr1)):
            x=str(arr1[i])
            for j in range(1,len(x)+1):
                d[x[:j]]=1
        for i in range(len(arr2)):
            x=str(arr2[i])
            for j in range(1,len(x)+1):
                if x[:j] in d:
                    m=max(m,len(x[:j]))
            # for
            # l1=len(x)
            # for j in range(len(arr2)):
            #     y=str(arr2[j])
            #     l2=len(y)
            #     if l1>l2:
            #         if x[:l2]==y:
            #             m=max(m,l2)
            #     elif l2>=l1:
            #         if y[:l1]==x:
            #             m=max(m,l1)
        return m

                    
        