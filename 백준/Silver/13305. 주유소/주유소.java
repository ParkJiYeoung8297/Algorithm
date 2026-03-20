// 가격이 낮은 곳에서 충전하는 것이 유리
// 왼쪽에서 오른쪽으로 이동해야한다.
// 뒤랑 비교했을 때, 가격이 비싸면 뒤에 갈만큼만 최소 주유 / 가격이 싸면 그 뒤랑 비교

// 스터디 피드백 :
// dp 이용하면 더 간단하게 구현 가능
// 2차원 dp면 10000을 보통 안넘음

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int city = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] distance = new int[city-1];
        for (int i = 0; i < distance.length; i++) {
            distance[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        int[] cost = new int[city];
        for (int i = 0; i < cost.length; i++) {
            cost[i] = Integer.parseInt(st.nextToken());
        }

        int oil = 0;
        int dist;
        int idx = 0;
        int pointer = 0;

        while (idx < distance.length) {
            dist = 0;
            while (cost[idx] <= cost[pointer] && pointer < distance.length) {
                dist += distance[pointer];
                pointer++;
            }
            oil += cost[idx] * dist;
            idx = pointer;
        }
        System.out.println(oil);
    }
}
