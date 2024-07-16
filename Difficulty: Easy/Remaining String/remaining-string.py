#User function Template for python3
class Solution:
	def printString(self, s, ch, count):
		d={}
		s=list(s)
		d[ch]=0
		for i in range(len(s)):
		    if s[i] in d:
		        d[s[i]]+=1
		        if d[s[i]]==count:
		            return "".join(s[i+1:])
		return ""
		        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()
        ch = input()[0]
        count = int(input())
        ob = Solution()
        answer = ob.printString(s, ch, count)

        print(answer)

# } Driver Code Ends