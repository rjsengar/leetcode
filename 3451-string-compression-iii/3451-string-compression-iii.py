class Solution:
    def compressedString(self, word: str) -> str:
        l=[]
        i=0
        while(i<len(word)):
            j=i+1
            s=word[i]
            while(j<len(word) and word[j]==s):
                j+=1
            if i+1==j:
                l.append('1')
                l.append(word[i])
                i+=1
            else:
                p=(j-i)
                while(p>9):
                    l.append('9')
                    l.append(word[i])
                    p-=9
                if p!=0:
                    l.append(str(p))
                    l.append(word[i])
                i=j
                
        return "".join(l)
        