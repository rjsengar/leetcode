import math
class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        l1=[]
        s=int(math.sqrt(r))
        def SieveOfEratosthenes(num):
            prime = [True for i in range(num+1)]
            p = 2
            while (p * p <= num):
                if (prime[p] == True):
                    for i in range(p * p, num+1, p):
                        prime[i] = False
                p += 1
            for p in range(2,num+1):
                if prime[p]:
                    l1.append(p)
        SieveOfEratosthenes(s+1)
        c=0
        # print(l1)
        for i in l1:
            if (i*i<=r and i*i>=l):
                c+=1
        return r-(l+c)+1
            
        