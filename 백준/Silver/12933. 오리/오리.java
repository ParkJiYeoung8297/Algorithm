// [그리디 문제]
// quack을 찾으려하지 말고, counting을 해라! (quack을 앞에서 부터 찾으면, u가 다른 오리의 울음인데 잘못 들어갔을 때, 틀린 답을 반환할 수 있음)
// q→u→a→c→k 순서니까, 이전 q가 있을 때만 u의 카운팅 증가시킴, 동시에 q는 카운팅 감소시킴 (사실상 u의 카운팅이 1이라는건 qu가 1개 있다는 것)
// 만약 q의 카운팅이 없는데 u가 등장했다면 불가능 반환 (ex. uqak)
import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] arr = br.readLine().split("");
        String[] letters = {"q","u","a","c","k"};
        int[] counts=new int[5];

        int current=0;
        int ducks=0;

        for (int i=0;i< arr.length;i++){
            boolean isFound=false;
            for (int idx=0;idx<letters.length;idx++){
                if (arr[i].equals(letters[idx])){
                    isFound=true;
                    if (arr[i].equals("q")){
                        counts[0]++;
                        current++;
                        ducks = Math.max(ducks,current);
                        break;
                    }

                    // 이전이 없는데 다음 요소가 나오면 불가능 반환
                    if (counts[idx-1]==0){
                        System.out.println(-1);
                        return;
                    }

                    if (arr[i].equals("k")){
                        current--;
                        counts[idx-1]--;
                    } else{
                        counts[idx-1]--;
                        counts[idx]++;
                    }
                    break;
                }
            }

            if (!isFound){
                System.out.println(-1);
                return;
            }
        }
        // 마지막 index는 사용안함
        for (int idx=0;idx<counts.length-1;idx++){
            if (counts[idx]!=0){
                System.out.println(-1);
                return;
            }
        }
        System.out.println(ducks);
    }

}
