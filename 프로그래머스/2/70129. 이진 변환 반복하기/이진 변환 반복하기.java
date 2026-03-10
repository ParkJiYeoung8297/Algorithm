// String → List 변환 : Arrays.asList(String_변수명)
// 0의 개수 세기 : Collections.frequency(List_변수명, "0")
// 배열은 연속적으로 저장되어있어, 주소 + index로 바로 접근한다 → O(1)
import java.util.*;

class Solution {
    public int[] solution(String s) {
        int[] answer = {0,0};
        while(!s.equals("1")){
            answer[1] += getRemovedZeroCount(s);
            answer[0]++;
            s = removedZero(s);
            s = getBinary(s);
        }
        return answer;
    }
    
    private String removedZero(String s1){
        return s1.replaceAll("0","");
    }
    
    private String getBinary(String s1){
        return Integer.toBinaryString(s1.length());
    }
    
    private int getRemovedZeroCount(String s1){
        return Collections.frequency(Arrays.asList(s1.split("")),"0");      
    }
    

    
}