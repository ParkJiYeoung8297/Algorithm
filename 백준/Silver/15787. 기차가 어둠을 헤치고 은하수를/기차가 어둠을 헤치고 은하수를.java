// x번째 좌석에 사람을 태워라. 이미 사람이 있으면 노 행동
// x번째 좌석에 사람을 내려라. 사람이 없다면 노 행동
// 모두 한칸씩 뒤로간다. 20번째 사람이 있다면 다음에 하차
// 모두 한칸씩 앞으로간다. 1번째에 사람이 있다면 다음에 하차

// 상태가 동일하면 건널 수 없다.

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        boolean[][] trains = new boolean[n + 1][21];


        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            String choice = st.nextToken();
            if (choice.equals("1")) {
                moveOne(trains, Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            } else if (choice.equals("2")) {
                moveTwo(trains, Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            } else if (choice.equals("3")) {
                moveThree(trains, Integer.parseInt(st.nextToken()));
            } else if (choice.equals("4")) {
                moveFour(trains, Integer.parseInt(st.nextToken()));
            }
        }

        HashSet<String> answer = new HashSet<>();

        for (int i = 1; i < n + 1; i++) {
            StringBuilder sb = new StringBuilder();
            for (int j = 1; j < 21; j++) {
                sb.append(trains[i][j] ? '1' : '0');
            }
            answer.add(sb.toString());
        }

        System.out.println(answer.size());
    }

    private static void moveOne(boolean[][] train, int trainNum, int idx) {
        if (!train[trainNum][idx]) {
            train[trainNum][idx] = true;
        }
    }

    private static void moveTwo(boolean[][] train, int trainNum, int idx) {
        if (train[trainNum][idx]) {
            train[trainNum][idx] = false;
        }
    }

    private static void moveThree(boolean[][] train, int idx) {
        for (int i = 20; i > 0; i--) {
            train[idx][i] = train[idx][i - 1];
        }
        train[idx][1] = false;
    }


    private static void moveFour(boolean[][] train, int idx) {
        for (int i = 1; i < 20; i++) {
            train[idx][i] = train[idx][i + 1];
        }
        train[idx][20] = false;
    }
}
