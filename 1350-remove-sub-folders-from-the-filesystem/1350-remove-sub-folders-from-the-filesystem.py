class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        l=[]
        folder.sort()
        for i in range(len(folder)):
            if l==[] or folder[i][:len(l[-1])]!=l[-1]:
                l.append(folder[i])
            if  l and len(folder[i])>len(l[-1]):
                    if folder[i][len(l[-1])]!='/':
                        l.append(folder[i])
        return l
            
            
            
        