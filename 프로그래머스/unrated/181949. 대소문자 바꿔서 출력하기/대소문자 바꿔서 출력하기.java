import java.util.Scanner;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        System.out.print(change(a));
    }
    static String change(String sc){
        char s;
        String result = "";
        for(int i = 0; i<sc.length(); i++){
            s = sc.charAt(i);
//            System.out.print(s);
            if(Character.isUpperCase(s)){
                result += Character.toLowerCase(s);
            }
            else if(Character.isLowerCase(s)){
                result += Character.toUpperCase(s);
            }
        }
        return result;
    }
}