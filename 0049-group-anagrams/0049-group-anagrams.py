class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            m=sorted(i)
            m="".join(m)
            if m in d:
                d[m].append(i)
            else:
                d[m]=[i]
        return list(d.values())


                
        