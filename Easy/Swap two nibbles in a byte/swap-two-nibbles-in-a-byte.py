#User function Template for python3
class Solution:
    def swapNibbles (self, n):
        b=bin(n).replace("0b","")
        
        if len(b)%8!=0:
            a=8-len(b)%8
            b=("0"*a)+b
        l=len(b)//2
        #print(b)
        s1=b[:l]
        s2=b[l:]
        s2+=s1
        k=int(s2,2)
        return k


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        print(ob.swapNibbles(n))

# } Driver Code Ends