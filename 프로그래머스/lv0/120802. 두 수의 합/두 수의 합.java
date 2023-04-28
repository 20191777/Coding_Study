import java.util.Scanner;

class Solution {
    public static int solution(int num1, int num2) {
        int answer = -1;
        
        answer = num1 + num2;
        
        return answer;
    }
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        int num1 = scan.nextInt();
        int num2 = scan.nextInt();
        
        System.out.println(solution(num1, num2));
    }
}
