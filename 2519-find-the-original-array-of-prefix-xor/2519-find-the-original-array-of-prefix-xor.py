class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        l=[]
        l.append(pref[0])
        for i in range(1,len(pref)):
            l.append(pref[i]^pref[i-1])
        return l
        