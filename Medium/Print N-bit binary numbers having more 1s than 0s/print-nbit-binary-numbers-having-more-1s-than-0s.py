#User function Template for python3
class Solution:
    def NBitBinary(self, n):
        l=[]
        a=2**n
        for i in range(a-1,0,-1):
            b=bin(i).replace("0b","")
            if len(b)!=n:
                b=(n-len(b))*'0'+b
            c1=0
            c2=0
            c3=0
            for j in b:
                if j=='0':
                    c1+=1
                if j=='1':
                    c2+=1
                if c2>=c1:
                    c3+=1
                if c1>c2:
                    break
            if c3==len(b):
                l.append(b)
        l.sort(reverse=True)
        return l





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()	
		answer = ob.NBitBinary(n)
		for value in answer:
			print(value,end=" ")
		print()


# } Driver Code Ends