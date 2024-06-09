class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        if len(hand)%groupSize!=0:
            return False
        l=[[]]
        p=0
        for i in range(len(hand)):
            t=1
            for j in l:
                if j==[] or j[-1]==hand[i]-1 and len(j)<groupSize:
                    j.append(hand[i])
                    t=0
                    p+=1
                    break
            if t==1 and len(j)!=groupSize and j[-1]+2<hand[i]:
                return False
            if t==1:
                l.append([hand[i]])
                p+=1
        if p!=len(hand):
            return False
        # print(l)
        for i in l:
            if len(i)!=groupSize:
                return False
        return True

        