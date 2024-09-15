class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        c=0
        left=cStart
        right=cStart+1
        top=rStart
        bottom=rStart+1
        l=[]
        while(c<rows*cols):
            for i in range(left,right+1):
                if top>=0 and top<rows and i>=0 and i<cols:
                    l.append([top,i])
                    c+=1
            top+=1
            for i in range(top,bottom+1):
                if i>=0 and i<rows and right>=0 and right<cols:
                    l.append([i,right])
                    c+=1
            top-=2
            right-=1
            
            for i in range(right,left-2,-1):
                if bottom>=0 and bottom<rows and i>=0 and i<cols:
                    l.append([bottom,i])
                    c+=1
            right+=2
            bottom-=1
            left-=1
            for i in range(bottom,top,-1):
                if i>=0 and i<rows and left>=0 and left<cols:
                    l.append([i,left])
                    c+=1
            bottom+=2

        return l

                
            


        