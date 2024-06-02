class Solution {
    public void reverseString(char[] s) {
       
        char temp;
        int l=s.length;
        int j,i=0;
        j=l-1;
        while(i<j)
        {
            temp=s[i];
            s[i]=s[j];
            s[j]=temp;
            i+=1;
            j-=1;
        }       
    }
    }
