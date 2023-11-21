#User function Template for python3

#User function Template for python3
from itertools import permutations
class Solution:
    def permutation(self,s):
        l1=len(s)
        l=[]
        c=0
        s1=""
        p=permutations(s)
        for i in list(p):
            for j in i:
                if j.isalpha():
                    s1+=j
        s2=""
        for i in s1:
            c+=1
            s2+=i
            if c==l1:
                l.append(s2)
                c=0
                s2=""
        l.sort()
        return l
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    while(T>0):
        s=input()
        ob=Solution()
        ans=ob.permutation(s)
        for i in ans:
            print(i,end=" ")
        print()
        
        T-=1
# } Driver Code Ends