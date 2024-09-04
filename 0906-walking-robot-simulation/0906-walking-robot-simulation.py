class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        di='N'
        m=0
        x,y=0,0
        d={}
        for i,j in obstacles:
            a=(i**2+j**2)
            if a not in d:
                d[a]=[[i,j]]
            else:
                d[a].append([i,j])
        for i in commands:
            if di=='N':
                if i==-1:
                    di='E'
                elif i==-2:
                    di='W'
                else:
                    for i in range(1,i+1):
                        a=x**2+(y+1)**2
                        if a in d and [x,y+1] in d[a]:
                            break
                        else:
                            y+=1
                        
            elif di=='S':
                if i==-1:
                    di='W'
                elif i==-2:
                    di='E'
                else:
                    for i in range(1,i+1):
                        a=x**2+(y-1)**2
                        if a in d and [x,y-1] in d[a]:
                            break
                        else:
                            y-=1
            elif di=='E':
                if i==-1:
                    di='S'
                elif i==-2:
                    di='N'
                else:
                    for i in range(1,i+1):
                        a=(x+1)**2+y**2
                        if a in d and [x+1,y] in d[a]:
                            break
                        else:
                            x+=1
                        
            elif di=='W':
                if i==-1:
                    di='N'
                elif i==-2:
                    di='S'
                else:
                    for i in range(1,i+1):
                        a=(x-1)**2+y**2
                        if a in d and [x-1,y] in d[a]:
                            break
                        else:
                            x-=1
            
            m=max((x**2+y**2),m)
        return m
            
            

        