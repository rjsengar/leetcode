#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        q=[]
        q.append(0)
        l=[]
        d1={}
        while(len(q)):
            n=q[0]
            l.append(n)
            if n not in d1:
                d1[n]=1
               
            q.remove(q[0])
            for i in adj[n]:
                if i not in d1:
                    q.append(i)
                    d1[i]=1
        return l
        
            
        





#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends