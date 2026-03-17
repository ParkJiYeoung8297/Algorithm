// (피드백) 리스트 보다는 배열을 사용하는 것이 좋음
// 배수 관련 문제에서는 해당 수에서 배수의 값만큼 인덱스를 더해서 값을 갱신해주면 더 빠름, 3의 배수일 때 3에서 시작해서 3 → 3+3 → 3+3+3
// BufferedReader, StringTokenizer, StringBuilder 공부하기
// psvm → public main 메서드 단축키
// command + shift + enter : 맨 끝에 자동완성 느낌 (;이나 괄호 생성해줌)
// command + d : 커서가 있는 줄 복사
// StringBuilder : 문자열을 mutable하게 사용할 때 사용 (String 값을 바꿔도 새로운 객체 할당 안함)


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int count = Integer.parseInt(br.readLine());

        int[] arr = new int[count + 1];
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 1; i < arr.length; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int studentCount = Integer.parseInt(br.readLine());

        while (studentCount-- > 0) {
            st = new StringTokenizer(br.readLine());
            int gender = Integer.parseInt(st.nextToken());
            int index = Integer.parseInt(st.nextToken());

            if (gender == 1) {
                changeBoy(arr, index);
                continue;
            }
            changeGirl(arr, index);
        }

        for (int i = 1; i < arr.length; i++) {
            sb.append(arr[i]).append(" ");
            if (i % 20 == 0) {
                sb.append("\n");
            }
        }
        System.out.println(sb);
    }

    private static void changeBoy(int[] arr, int index) {
        for (int i = index; i < arr.length; i++) {
            if (i % index == 0) {
                arr[i] = 1 - arr[i];
            }
        }
    }

    private static void changeGirl(int[] arr, int index) {
        int p1 = index - 1;
        int p2 = index + 1;
        arr[index]=1-arr[index];

        while(p1>=1 && p2<arr.length){
            if (arr[p1]==arr[p2]){
                arr[p1] = 1 - arr[p1];
                arr[p2] = 1 - arr[p2];
                p1--;
                p2++;
                continue;
            }
            break;
        }

    }
}
