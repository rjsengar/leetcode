#User function Template for python3
from itertools import permutations

class Solution:
    def find_permutation(self, S):
        l1=[]
        q=[]
        l=list(S)
        p=permutations(l)
        for i in list(p):
            g="".join(i)
            if g not in set(q):
                q.append(g)
                l1.append(g)
        l1.sort()
        return l1
        
        






#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		ans.sort()
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends