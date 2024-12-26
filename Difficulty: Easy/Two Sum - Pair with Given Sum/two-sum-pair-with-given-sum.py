#User function Template for python3
class Solution:
	def twoSum(self, arr, target):
	    d={}
	    for i in arr:
	        if i not in d:
	            d[i]=1
	        else:
	            d[i]+=1
	    for i in arr:
	        if (target-i) in d and (target-i)==i and d[i]>1:
	            return True
	        elif target-i in d and (target-i)!=i:
	            return True
	    return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3


def main():
    T = int(input())
    while T > 0:
        x = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.twoSum(arr, x)
        if ans:
            print("true")
        else:
            print("false")
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends