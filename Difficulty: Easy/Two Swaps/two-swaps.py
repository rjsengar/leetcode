class Solution:
    def checkSorted(self, arr):
        d={}
        c=0
        n=len(arr)
        for i in range(len(arr)):
            d[arr[i]]=i
        # print(d)
        for i in range(len(arr)):
            if arr[i]!=i+1:
                a=d[i+1]
                d[arr[i]],d[i+1]=d[i+1],d[arr[i]]
                arr[i],arr[a]=arr[a],arr[i]
                c+=1
                # print(d)
            if c>2:
                return False
        if c<=2 and c%2==0:
            return True
        return False
            

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().split()))

        sol = Solution()
        result = sol.checkSorted(arr)
        if result:
            print("true")
        else:
            print("false")

# } Driver Code Ends