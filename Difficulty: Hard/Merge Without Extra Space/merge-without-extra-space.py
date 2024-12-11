class Solution:
    def mergeArrays(self, a, b):
        c=a+b
        c.sort()
        # print(c)
        for i in range(len(a)):
            a[i]=c.pop(0)
        for i in range(len(b)):
            b[i]=c.pop(0)
        
        


#{ 
 # Driver Code Starts
# Input handling and main function
if __name__ == "__main__":
    # Number of test cases
    t = int(input().strip())

    for _ in range(t):
        # Input first array
        a = list(map(int, input().strip().split()))
        # Input second array
        b = list(map(int, input().strip().split()))

        # Create solution object and merge the arrays
        solution = Solution()
        solution.mergeArrays(a, b)

        # Output both arrays in the same line space-separated
        print(" ".join(map(str, a)))
        print(" ".join(map(str, b)))

# } Driver Code Ends