# User function Template for python3

class Solution:
    def toh(self, N, fromm, to, aux):
        c=0
        def TowerOfHanoi(n , source, destination, auxiliary):
            nonlocal c
            if n==1:
                print ("move disk 1 from rod",source,"to rod",destination)
                c+=1
                return
            TowerOfHanoi(n-1, source, auxiliary, destination)
            print ("move disk",n,"from rod",source,"to rod",destination)
            c+=1
            TowerOfHanoi(n-1, auxiliary, destination, source)
        TowerOfHanoi(N , fromm, to, aux)
        return c





#{ 
 # Driver Code Starts
# Initial Template for Python 3


import math


def main():

    T = int(input())

    while(T > 0):
        N = int(input())
        ob = Solution()
        print(ob.toh(N, 1, 3, 2))
        T -= 1
if __name__ == "__main__":
    main()


# } Driver Code Ends