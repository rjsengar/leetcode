class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m=len(box)
        n=len(box[0])
        l=[]
        for i in range(m):
            c=0
            for j in range(n):
                if box[i][j]=='#':
                    c+=1
                    box[i][j]="."
                if box[i][j]=='*' or j==n-1:
                    if box[i][j]=='*':
                        k=j-1
                    else:
                        k=j
                    while(c):
                        box[i][k]='#'
                        k-=1
                        c-=1
                    

        for i in range(n):
            l1=[]
            for j in range(m):
                l1.append(box[j][i])
            l.append(l1[::-1])
        return l
            
        