class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        s=[]
        s=[1]
        l=[]
        j=0
        l.append("Push")
        i=2
        p=0
        while(i<=n and j<len(target)):
            #print(s)
            if len(s)>p and s and s[-1]!=target[j]:
                s.pop()
                l.append("Pop")
            if s==[] or s[-1]<target[j]:
                s.append(i)
                i+=1
                l.append("Push")
            if s[-1]==target[j]:
                j+=1
                p+=1
            # else: #s[-1]>target[j] and s[-1]!=target[j]:
            #     s.pop()
            #     l.append("Pop")
            # elif s[-1]==target[j]:
            #     j+=1
            if s==target:
                return l
        return l

        