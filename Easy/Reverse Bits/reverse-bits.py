#User function Template for python3

class Solution:
    def reversedBits(self, X):
        b=bin(X).replace("0b","")
        b='0'*(32-len(b))+b
        b=b[::-1]
        a=int(b,2)
        return a
        





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X=int(input())
        
        ob = Solution()
        print(ob.reversedBits(X))
# } Driver Code Ends