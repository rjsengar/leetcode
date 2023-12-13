#User function Template for python3

class Solution:
    # A1[] : the input array-1
    # N : size of the array A1[]
    # A2[] : the input array-2
    # M : size of the array A2[]
    
    #Function to sort an array according to the other array.
    def relativeSort (self,A1, N, A2, M):
        l=[]
        d={}
        for i in A1:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
                
        for i in A2:
            if i in d:
                while(d[i]):
                    l.append(i)
                    d[i]-=1
        A1.sort()
        for i in A1:
            if d[i]>=1:
                l.append(i)
        A1=l[:]
        return l
        
    





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int (input ())
    while t > 0:
        n, m = list(map(int, input().split()))
        a1 = list(map(int, input().split()))
        a2 = list(map(int, input().split()))
        
        ob=Solution()
        a1 = ob.relativeSort (a1, n, a2, m)
        print (*a1, end = " ")
        
        print ()
        
        t -= 1

# } Driver Code Ends