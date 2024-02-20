#User function Template for python3

class Solution:
    def wordBreak(self, n, s, dictionary):
        l=[]
        m=""
        for i in dictionary:
            if i[0]==s[0]:
                l.append(i)
        while(l):
            a=l.pop()
            if len(a)>len(s) :
                continue
            le=len(a)
            if a==s:
                return True
            for i in dictionary:
                if le<len(s) and len(i) and  s[le]==i[0]:
                    if a+i==s:
                        return True
                    m=a+i
                    if m==s[:len(m)]:
                        l.append(m)
                if m==s:
                    return True
        return False
            
            
            
            
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		n = int(input())
		dictionary = [word for word in input().strip().split()]
		s = input().strip()
		ob = Solution()
		res = ob.wordBreak(n, s, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends