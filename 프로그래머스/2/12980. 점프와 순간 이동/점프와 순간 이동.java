// [이진 탐색]
// 순간이동을 이용하는 것이 제일 에너지를 적게 사용하는 방법
// 이진 탐색하고 남은 값은 에너지 사용
import java.util.*;

public class Solution {
    public int solution(int n) {
        int ans = 0;

        while (n!=0){
            if (n%2==0){
                n=n/2;
                continue;
            }
            n-=1;
            ans+=1;
        }

        return ans;
    }
}