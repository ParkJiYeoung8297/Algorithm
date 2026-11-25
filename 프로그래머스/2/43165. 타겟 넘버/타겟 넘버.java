// dfs 완전 탐색
// 양수, 음수 2가지 방법으로 나뉘어짐
import java.util.*;
class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        Stack<int[]> stack = new Stack<>();
        stack.push(new int[]{0,0}); // 합, idx
        
        while(!stack.isEmpty()){
            int[] result = stack.pop();
            
            if (result[1] == numbers.length){
                if (target == result[0]){
                    answer = answer+1;
                }
                continue;
            }
            
            stack.push(new int[]{result[0] + numbers[result[1]], result[1] + 1});
            stack.push(new int[]{result[0] - numbers[result[1]], result[1] + 1});
        }
        return answer;
    }
}