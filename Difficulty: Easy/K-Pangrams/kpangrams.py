#User function Template for python3
class Solution:
    def kPangram(self,string, k):
        d={}
        c=0
        for i in string:
            if i!=' ':
                c+=1
                d[i]=1
        if (len(d)+k)>=26 and c>=26:
            return True
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        string = input()
        K = int(input())
        ob = Solution()
        a = ob.kPangram(string, K)
        if a:
            print("true")
        else:
            print("false")

# } Driver Code Ends