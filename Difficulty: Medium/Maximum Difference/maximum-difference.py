class Solution:
    def findMaxDiff(self, arr):
        l1=[]
        for i in range(len(arr)):
            p=0
            for j in range(i+1,len(arr)):
                if arr[i]>arr[j]:
                    l1.append(arr[j])
                    p=1
                    break
            if p==0:
                l1.append(0)
        l2=[]
        for i in range(len(arr)):
            p=0
            for j in range(i,-1,-1):
                if arr[i]>arr[j]:
                    l2.append(arr[j])
                    p=1
                    break
            if p==0:
                l2.append(0)
        m=0
        for i in range(len(l1)):
            m=max(m,abs(l1[i]-l2[i]))
        # print(l1,l2)
        return m
        # st=[]
        # st1=[]
        # l1=[]
        # for i in arr[::-1]:
        #     if st==[]:
        #         if st1==[]:
        #             l1.append(0)
        #         else:
        #             l1.append(st1[-1])
        #         st.append(i)
        #     elif st[-1]<i:
        #         l1.append(st[-1])
        #         if i<st1[-1]:
        #             st1.append(i)
        #         st.append(i)
        #     else:
        #         p=0
        #         while(st):
        #             k=st.pop()
        #             if k<i:
        #                 l1.append(k)
        #                 st.append(i)
        #                 p=1
        #                 break
        #         if p==0:
        #             l1.append(0)
        #             st.append(i)
        # print(l1)
        return 3


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.findMaxDiff(arr))

# } Driver Code Ends