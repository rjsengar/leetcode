class Solution:
    def countSeniors(self, details: List[str]) -> int:
        l=[]
        for i in details:
            for j in range(len(i)):
                if i[j].isalpha():
                    l.append(int(i[j+1:j+3]))
                    break
        c=0
        for i in l:
            if i>60:
                c+=1
        return c
            
