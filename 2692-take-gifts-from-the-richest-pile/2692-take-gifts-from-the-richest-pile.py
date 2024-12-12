class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        c=0
        while(k):
            m=max(gifts)
            i=gifts.index(m)
            gifts[i]=int(m**(0.5))
            k-=1
        s=sum(gifts)
        return s
        