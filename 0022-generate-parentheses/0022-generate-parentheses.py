class Solution:
    def generateParenthesis(self, n):
        if n == 0:
            return ['']
        return ['(' + left + ')' + right
                for i in range(n)
                for left in self.generateParenthesis(i)
                for right in self.generateParenthesis(n - i - 1)]
        