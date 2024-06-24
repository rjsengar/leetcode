#User function Template for python3
class Solution:
	def bracketNumbers(self, str):
	    l=[]
	    c=0
	    p=0
	    s=""
		for i in str:
		    if i=='(':
		        s+=i
		    elif i==')':
		        s+=i
		i=0
		l1=[]
		l=[]
# 		print(s)
		while(i<len(s)):
		    if s[i]=='(':
		        c+=1
		        l.append(c)
		        l1.append(c)
		        i+=1
		    else:
		        l1.append(l.pop())
		        i+=1
		    
		return l1
		        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.bracketNumbers(S)
        for value in answer:
            print(value, end=" ")
        print()

# } Driver Code Ends