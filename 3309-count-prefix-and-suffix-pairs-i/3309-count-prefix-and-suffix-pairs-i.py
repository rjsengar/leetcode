class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        c=0
        for i in range(len(words)):
            l1=len(words[i])
            s1=words[i]
            for j in range(i+1,len(words)):
                s2=words[j]
                if (l1<=len(s2)) and (s2[:l1]==s1) and (s2[len(s2)-l1:]==s1):
                    c+=1
        return c
        