class Solution:
    def intToRoman(self, num: int) -> str:
        r_s=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        r_v=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        s=""
        i=0
        while(num>0):
            while(num>=r_v[i]):
                s+=r_s[i]
                num-=r_v[i]
            i+=1
        return s
        