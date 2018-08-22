import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the alternatingCharacters function below.
    int alternatingCharacters(String s) {
       // char arr=new char[s.length()];
        int count=0;
        //arr=s.toCharArray();
        System.out.println(s.length());
        for(int j=0,i=1;j<s.length()-1 || i<s.length();j++,i++)
        {
             System.out.println("iteration no "+j);
             System.out.println("iteration no "+i);
            System.out.println(s.charAt(j) + "and sec char "+ s.charAt(i));
            if (s.charAt(j)==s.charAt(i)){
                ++count;
                System.out.println(count);
            }
        }
        //for (int i=0;i<arr.ARRAYLENGTH;i++){
          //  if (arr[i]==arr[i+1]){
            //    arr = ArrayUtils.removeElement(arr,arr[i]);
            //}
                
           // }
            return count;
        }

    

   // private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        Solution s1=new Solution();
        int result=s1.alternatingCharacters("AAAA");
        System.out.println(result);
    }
}
