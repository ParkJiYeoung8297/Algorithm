// Arrays.asList(String_Array_변수명) → 불변 리스트
// new ArrayList<>(List_변수명) → 가변 리스트
// stack에 제거되지 않은 요소를 담고, 현재 문자와 stack[-1]과 비교
// array는 chars[1]로 접근하고, list는 chars.get(1)로 접근한다.
// deque는 get으로 조회가 안된다. deque_변수명_peekFirst(), deque_변수명_peekLast()로만 가능

import java.util.*;

class Solution
{
    public int solution(String s)
    {
        int idx=0;
        String[] chars= s.split("");
        Deque<String> stack=new LinkedList<>();
        
        for (String s1:chars){
            if (!stack.isEmpty() && stack.peekLast().equals(s1)){
                stack.pollLast();
            }
            else{
                stack.addLast(s1);
            }
        }
        
        return stack.isEmpty() ? 1 : 0;
    }
}