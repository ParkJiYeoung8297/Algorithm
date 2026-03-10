// String → List 변환 : Arrays.asList(String_변수명)
// 0의 개수 세기 : Collections.frequency(List_변수명, "0")
// 배열은 연속적으로 저장되어있어, 주소 + index로 바로 접근한다 → O(1)

// 변경된 방법 : 0의 개수를 세지 않고, 원래 길이에서 0을 제거한 후 length()를 빼주면 된다.
import java.util.*;

class Solution {
    public int[] solution(String s) {
        int[] answer = {0,0};
        while(!s.equals("1")){
            answer[1]+=s.length();
            s=removedZero(s);
            answer[1] -= s.length();
            s = getBinary(s);
            answer[0]++;
        }
        return answer;
    }
    
    private String removedZero(String s1){
        return s1.replace("0","");
    }
    
    private String getBinary(String s1){
        return Integer.toBinaryString(s1.length());
    }
    
}