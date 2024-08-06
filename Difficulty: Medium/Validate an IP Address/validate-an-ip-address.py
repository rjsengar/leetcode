#User function Template for python3
class Solution:
    def isValid(self, str):
        s1=str.split('.')
        if len(s1)!=4:
            return False
        # print(s1)
        for i in s1:
            if not(i and int(i)>=0 and int(i)<=255):
                return False
            if len(i)>1 and i[0]=='0':
                return False
            # if i and len(i)>1 and i[0]='0':
            #     return False
        return True
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        ob = Solution()
        if (ob.isValid(s)):
            print("true")
        else:
            print("false")

# } Driver Code Ends