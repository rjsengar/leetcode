#User function Template for python3
class Solution:
    def sameFreq(self, s):
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l=list(d.values())
        d1={}
        # print(l)
        if len(set(l))==1:
            return True
        if len(set(l))==2:
            s1=list(set(l))
            # print(l)
            # print(s1)
            if l.count(s1[0])==len(d)-1:
                if s1[1]-s1[0]==1 or s1[1]==1:
                    return True
            if l.count(s1[1])==len(d)-1:
                if s1[0]-s1[1]==1 or s1[0]==1:
                    return True
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	T=int(input())

	for _ in range(T):
		s = input()
		ob = Solution()
		answer = ob.sameFreq(s)
		if answer:
			print(1)
		else:
			print(0)

# } Driver Code Ends