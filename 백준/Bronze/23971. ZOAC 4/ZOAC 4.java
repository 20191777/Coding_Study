import java.util.Scanner;
public class Main {
    public int solution(int H, int W, int N, int M){
        int r = (H-1)/(N+1)+1;
        int l = (W-1)/(M+1)+1;
        return r*l;
    }

    public static void main(String[] args) {
        int H, W, N, M;
        Scanner scan = new Scanner(System.in);
        H = scan.nextInt();
        W = scan.nextInt();
        N = scan.nextInt();
        M = scan.nextInt();

        Main sol = new Main();

        System.out.println(sol.solution(H, W, N, M));
    }
}