#User function Template for python3
class Solution:
	def removeDups(self, str):
		d={}
		s1=""
		for i in str:
		    if i not in d:
		        s1+=i
		        d[i]=1
		return s1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.removeDups(s)

        print(answer)

# } Driver Code Ends