class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        s1='aeiou'
        l1=[]
        l2=[]
        l=[]
        for i in words:
            if i[0] in s1 and i[-1] in s1:
                l1.append(1)
            else:
                l1.append(0)
        # print(l1)
        s=0
        for i in l1:
            s+=i
            l.append(s)
        for i in queries:
            if i[0]!=0:
                l2.append(l[i[1]]-l[i[0]-1])
            else:
                l2.append(l[i[1]])
        return l2
        