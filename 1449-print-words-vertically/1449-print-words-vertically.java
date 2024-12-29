class Solution {
    public List<String> printVertically(String s) {
       String[] array = s.split(" ");
        int i=0;
        String res=" ";
        int mal=0;
        int mil=999;
        for(String str : array)
        {
            mal =Math.max(str.length(),mal);
            mil =Math.min(str.length(),mil);
        }
        ArrayList<String> result= new ArrayList<>();
        for(i=0;i<mal;i++)
        {
            res="";
            for(int j=0;j<array.length;j++)
            {
                if(i<array[j].length())
                {
               
                String word=array[j];
                res+=word.charAt(i);
                }
                else{
                  res+=" ";
                }
            }
            int m=0;
            m=res.length();
            int k=m-1;
            for(k=m-1;k>=0;k--){
                if (res.charAt(k)!=' ')
                break;
            }

            res=res.substring(0,k+1);
            result.add(res);
        }
        return result;
    }
}