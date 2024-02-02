#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,s):
        c=0
        for i in s:
            if not(i.isdigit()):
                c+=1
        if (c==1 and s[0]=='-') or c==0:
            return int(s)
        return -1


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends