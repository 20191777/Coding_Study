import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {
    public void solution(int a, int b, int c){
        int max = Math.max(Math.max(a,b),c);
//        System.out.println(a + " " + b + " " + c);
        if(max == a && max>=b+c) {
            System.out.println("Invalid");
            return;
        }
        if(max == b && max>=a+c){
            System.out.println("Invalid");
            return;
        }
        if(max == c && max>=b+a){
            System.out.println("Invalid");
            return;
        }

        if(a==b && b==c && c==a){
            System.out.println("Equilateral");

        }
        else if((a==b && b!=c) || (a!=b && b==c)
                || (a!=b && c==a)){
            System.out.println("Isosceles");

        }
//        else if(max < a + b && max < c + b && max < a + c){
//            System.out.println("Scalene");
//        }
        else if(a!=b && a!=c && b!=c){
            System.out.println("Scalene");
            
        }

    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str;

        int a, b, c;
        Scanner scan = new Scanner(System.in);
        while(true){

            str = br.readLine().split(" ");
            a = Integer.parseInt(str[0]);
            b = Integer.parseInt(str[1]);
            c = Integer.parseInt(str[2]);

            if(a==0 && b==0 && c==0)
                break;

            Main sol = new Main();
            sol.solution(a, b, c);
        }
    }
}