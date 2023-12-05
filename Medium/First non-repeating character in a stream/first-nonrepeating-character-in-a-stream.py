#User function Template for python3

class Solution:
    def FirstNonRepeating(self, A):
        l=[]
        c=[0]*26
        res=""
        for i in A:
            if(c[ord(i)-ord("a")]==0):
                l.append(i)
            c[ord(i)-ord("a")]+=1
            while(l!=[] and c[ord(l[0])-ord("a")]>1):
                l.pop(0)
            if(l==[]):
                res+="#"
            else:
                res+=l[0]
        return res





#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = input()
		ob = Solution()
		ans = ob.FirstNonRepeating(A)
		print(ans)

# } Driver Code Ends