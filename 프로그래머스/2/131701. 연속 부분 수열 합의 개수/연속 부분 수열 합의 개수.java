// [슬라이딩 윈도우 + 원형 배열]
// set을 이용해서 중복없는 합의 개수를 구한다. 
// 이때, 합의 시간을 줄이기 위해 앞 요소 뺴고, 뒤 요소 더하는 방식으로 구한다. (슬라이딩 윈도우)
// 원형 배열 처리 → 배열을 2배로 늘리기
// "java.util.*" 에는 "java.util.stream.Collectors"가 포함되어있지 않다.
// (보충) 지금은 리스트를 사용했지만, 보통 배열 * 2를 한 후에 값을 for문으로 넣어준다.(int[] arr = new int[n * 2]) → 배열 값을 바꾸지 않기 때문

import java.lang.*;
import java.util.*;
import java.util.stream.Collectors;
    
class Solution {
    public int solution(int[] elements) {

        List<Integer> doubleElement = new ArrayList<>();
        for (Integer e : elements){
            doubleElement.add(e);
        }
        doubleElement.addAll(new ArrayList<>(doubleElement)); // 원본 유지한채로 복사
        
        Set<Integer> el = new HashSet<Integer>();
        for (int len=1;len<=elements.length;len++){  // 길이
            int start = doubleElement.subList(0,len).stream()
                .mapToInt(Integer::intValue)
                .sum();
            el.add(start);
            
            for (int j=0;j<elements.length-1;j++){ // 시작 index
                start=start-doubleElement.get(j)+doubleElement.get(j+len);
                el.add(start);
            }
        }
        return el.size();
    }
}