class Solution:
    def isBalanced(self, num: str) -> bool:
        s1=0
        s2=0
        for i in range(len(num)):
            if i%2==0:
                s1+=int(num[i])
            else:
                s2+=int(num[i])
        if s1==s2:
            return True
        return False
        