class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        c=0
        l=[]
        l1=[]
        for i in words:
            if i[0] in 'aeiou' and i[-1] in 'aeiou':
                l1.append(1)
            else:
                l1.append(0)
        l2=[0]*(len(l1)+1)
        l2[0]=l1[0]
        for i in range(len(words)):
            l2[i+1] = l2[i]+l1[i]
        for x,y in queries:
            l.append(l2[y+1]-l2[x])
        return l
        