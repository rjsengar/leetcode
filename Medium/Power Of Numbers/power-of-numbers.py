#User function Template for python3

class Solution:
    #Complete this function
    def power(self,N,R):
        mod=(10**9)+7
        res=1
        #Your code here
        while(R>0):
            if(R%2==1):
                res=(res*N)%mod
            N=int((N*N)%mod)
            R//=2
        return(res)





#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends