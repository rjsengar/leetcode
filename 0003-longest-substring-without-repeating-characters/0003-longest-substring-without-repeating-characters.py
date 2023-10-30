class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        c=0
        s1=""
        for i in s:
            if i not in s1:
                s1+= i
            else:
                s1= s1[s1.index(i)+1:] + i
                #print(s1)
            if len(s1) > c:
                c = len(s1)
        return c
