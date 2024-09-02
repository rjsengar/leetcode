class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        i=0
        s=sum(chalk)
        k=k%s
        n=len(chalk)
        while(k>0):
            if (k-chalk[i])<0:
                return i
            else:
                k-=chalk[i]
                i+=1
                i=i%n
        return i

        