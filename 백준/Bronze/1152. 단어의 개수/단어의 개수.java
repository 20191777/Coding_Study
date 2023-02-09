import java.util.Scanner;

public class Main {
    public void solution() {
        Scanner scan = new Scanner(System.in);
        String words = scan.nextLine();

        words = words.trim();
        String[] words_arr = words.split(" ");

        int len = words_arr.length;
           
        if(words == ""){
            len = 0;
        }
        
        System.out.println(len);
    }
    public static void main(String[] args) {
        Main count = new Main();
        count.solution();
    }
}