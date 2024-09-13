#User function Template for python3

class Solution:
    def rearrange(self,arr):
        l1=[]
        l2=[]
        for i in arr:
            if i>=0:
                l1.append(i)
            else:
                l2.append(i)
        k=0
        j=0
        l3=[]
        for i in range(len(arr)):
            if i%2==0 and k<len(l1):
                l3.append(l1[k])
                k+=1
            elif i%2!=0 and j<len(l2):
                l3.append(l2[j])
                j+=1
            elif k<len(l1):
                l3.append(l1[k])
                k+=1
            else:
                l3.append(l2[j])
                j+=1
        for i in range(len(arr)):
            arr[i]=l3[i]
        return arr

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.rearrange(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends