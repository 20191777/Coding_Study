import java.util.Scanner;

public class Main {
    public void solution(int a, int b){
        System.out.print(a+b);
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Main p = new Main();
        int a = scan.nextInt();
        int b = scan.nextInt();
        p.solution(a, b);
    }
}