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
        return m

                    
        