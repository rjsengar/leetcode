class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        arr=[]
        R=n
        C=n
        mat=[[0 for x in range(n)] for y in range(n)] 
        n=n*n
        for i in range(1,n+1):
            arr.append(i)
        top = 0;
        bottom = R - 1;
        left = 0;
        right = C - 1;
    
        index = 0;
    
        while (True):
            
            if(left > right):
                break;
    
            # print top row
            for i in range(left, right + 1):
                mat[top][i] = arr[index];
                index += 1;
            top += 1;
    
            if (top > bottom):
                break;
    
            # print right column
            for i in range(top, bottom+1):
                mat[i][right] = arr[index];
                index += 1;
            right -= 1;
    
            if (left > right):
                break;
    
            # print bottom row
            for i in range(right, left-1, -1):
                mat[bottom][i] = arr[index];
                index += 1;
            bottom -= 1;
    
            if (top > bottom):
                break;
    
            # print left column
            for i in range(bottom, top-1, -1):
                mat[i][left] = arr[index];
                index += 1;
            left += 1;
        return mat