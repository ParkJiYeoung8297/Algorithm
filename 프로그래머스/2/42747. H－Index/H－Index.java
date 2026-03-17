// i를 기준으로 정렬하는 것이 편함 (한번에 체크 가능)
// 인덱스 i를 기준으로 i개, n-i개로 나뉘는데 (기준인 i는 제외)
// citations[i]는 citations[i] 뒤에 있는 수 중에서 가장 최소의 수이다. (정렬 했으니까)
// h=n-i이니까 n-i<=citations[i]이면, h 이상인게 h번 이상 발생한 것이다.


// 리스트는 출력하면 안에 요소가 나오지만,배열은 출력하면 메모리 주소가 나온다.
// 배열은 default toString([타입@해시코드])을 사용하고
// 리스트는 오버라이딩된 toString([내부 요소 출력])을 사용하기 때문이다.
// 배열에서 안에 요소 출력하려면 Arrays.toString(citations)을 해줘야한다.
import java.util.*;

class Solution {
    public int solution(int[] citations) {
        Arrays.sort(citations);
        for (int i=0;i<citations.length;i++){
            if (citations.length-i<=citations[i]){
                return citations.length-i;
            }
        }
        
        return 0;
    }
}