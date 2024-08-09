class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        x=points[0]
        c=1
        for i,j in points:
            if x[0]<=i and i<=x[1]:
                x[0]=max(x[0],i)
                if x[1]>j:
                    x[1]=j
            else:
                # print('g')
                x=[i,j]
                c+=1
            # print(x)
        return c
            
        