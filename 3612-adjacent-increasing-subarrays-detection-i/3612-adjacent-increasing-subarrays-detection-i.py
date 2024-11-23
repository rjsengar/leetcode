class Solution:
    def hasIncreasingSubarrays(self, arr: List[int], k: int) -> bool:
        l=[]
        d={}
        for i in range(len(arr)):
            c=1
            for j in range(i,len(arr)-1):
                if arr[j]<arr[j+1]:
                    c+=1
                else:
                    # print(c)
                    if c>=(2*k):
                        return True
                    else:
                        if c>=k:
                            # print('a')
                            d[i]=1
                    break
            if c>=2*k:
                return True
            else:
                if c>=k:
                    # print('a',c)
                    d[i]=1
        # if k==1:
        #     d[len(arr)-1]=1
        # print(d)
        for i in d:
            if i+k in d:
                return True
        return False

        return False

        