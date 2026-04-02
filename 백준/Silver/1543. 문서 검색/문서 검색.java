// substring보다 startwith으로 푸는 것이 좋음

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int answer = 0;

        String word =  br.readLine();
        String target = br.readLine();

        for (int i=0; i < word.length()-target.length()+1; i++) {
            if (word.startsWith(target, i)){
                answer++;
                i+=target.length()-1;
            }
        }
        System.out.println(answer);
    }
}
