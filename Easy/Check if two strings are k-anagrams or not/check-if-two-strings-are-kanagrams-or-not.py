#User function template for Python 3

class Solution:
    def areKAnagrams(self, str1, str2, k):
        c=0
        if len(str1)==len(str2):
            for i in str1:
                if i not in str2:
                    c+=1
                else:
                    str2=str2.replace(i,"",1)
            if c<=k:
                return True
            return False
        else:
            return False
                





#{ 
 # Driver Code Starts
#Initial template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        arr = input().strip().split()
        k = int(input())
        ob = Solution()
        if ob.areKAnagrams(arr[0], arr[1], k):
            print(1)
        else:
            print(0)
# } Driver Code Ends