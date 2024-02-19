#User function Template for python3

class Solution:
    def minValue(self, s, k):
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        l=[]
        c=0
        for i in d:
            l.append(d[i])
        l.sort(reverse=True)
        i=0
        while(k and i<len(l)):
            s1=l[0]
            j=i
            while(j<len(l) and l[j]==s1):
                l[j]=l[j]-1
                j+=1
                k-=1
                if k<=0:
                    break
            if k<=0:
                break
        for i in l:
            c+=i*i
        return c

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        k = int(input())
        
        ob = Solution()
        print(ob.minValue(s, k))
# } Driver Code Ends