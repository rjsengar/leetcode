class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        d={}
        n=len(arr)
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        l=[]
        for i in d:
            if d[i]>n/3:
                l.append(i)
        l.sort()
        return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends