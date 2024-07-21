#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def findMaxProduct(self, arr):
        arr.sort()
        c=0
        for i in arr:
            if i<0:
                c+=1
        if c%2!=0:
            c-=1
        c1=0
        s=1
        g=0
        for i in arr:
            if c1<c and i<0:
                s*=i
                c1+=1
                g=1
            elif i>=1:
                s*=i
                g=1
        if g==0:
            return max(arr)
        if s>=1000000007:
            return s%1000000007
        return s
            
    


#{ 
 # Driver Code Starts.
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        solution = Solution()
        ans = solution.findMaxProduct(arr)
        results.append(ans)
    
    for result in results:
        print(result)
# } Driver Code Ends