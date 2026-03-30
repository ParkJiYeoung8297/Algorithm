// 뒤에서 부터 stack에 저장
// 1) 비어있으면 저장, 2) stack 첫번째 수가 numbers[i]보다 크면 뒤큰수! 갱신하기
// 3) stack 첫번째 수가 numbers[i]보다 작으면, stack 갱신 
import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
        Arrays.fill(answer, -1);
        Deque<Integer> stack = new ArrayDeque<>();
        
        for (int i=numbers.length-1;i>=0;i--){
            if (stack.isEmpty()){
                stack.addFirst(numbers[i]);
                continue;
            }
            
            if (stack.peekFirst()>numbers[i]){
                answer[i]=stack.peekFirst();
                stack.addFirst(numbers[i]);
            }
            else {
                while(!stack.isEmpty() && stack.peekFirst()<=numbers[i]){
                    stack.pop();
                }
                if (!stack.isEmpty()){
                    answer[i]=stack.peekFirst();
                }
                stack.addFirst(numbers[i]);
            }
        }
        return answer;
    }
}