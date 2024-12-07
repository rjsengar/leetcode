#User function Template for python3

class Solution:
    def subsets(self, arr):
        
        arr=list(set(arr))
        arr.sort()
        n=len(arr)
        l=[]
        def solve(i,s):
            if i>=n:
                l.append(s[:])
                return
            s.append(arr[i])
            solve(i+1,s)
            s.pop()
            solve(i+1,s)
        solve(0,[])
        l.sort()
        return l





#{ 
 # Driver Code Starts
# Example to simulate input/output behavior:
if __name__ == "__main__":
    t = int(input())  # Number of test cases
    for _ in range(t):
        arr = list(map(int,
                       input().split())
                   )  # Reading the array input as space-separated integers

        ob = Solution()
        res = ob.subsets(arr)

        # Print result
        for subset in res:
            print(" ".join(map(str, subset)))
        print("~")

# } Driver Code Ends