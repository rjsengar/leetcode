class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d={}
        if arr.count(0)>1:
            return True
        for i in arr:
            d[i]=1
        for i in arr:
            if i*2 in d and i*2!=0:
                return True
        return False