//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader read =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            String s = read.readLine();
            char ch = read.readLine().charAt(0);
            int count = Integer.parseInt(read.readLine());
            Solution ob = new Solution();
            String result = ob.printString(s,ch,count);
            
            System.out.println(result);
        }
    }
}
// } Driver Code Ends




//User function Template for Java

class Solution {
    String printString(String S, char ch, int count) {
        StringBuilder sb = new StringBuilder();
        sb.append(S);
        int x = -1;
       for(int i = count; i!=0; i--){
           String st = sb.substring(x+1);
           x = st.indexOf(ch);
           if(x == -1){
               return "Empty string";
           }
           sb.delete(0, x+1);
           x = -1;
       }
       if(sb.length() == 0){
           return "Empty string";
       }
       return sb.substring(0);
    }
}