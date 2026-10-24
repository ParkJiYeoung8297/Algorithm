import java.util.*;
class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        Stack<int[]> stack = new Stack<>(); 
        stack.push(new int[]{numbers[0], 0}); // [총합, idx]
        stack.push(new int[]{-numbers[0], 0}); // [총합, idx]
        
        while (!stack.isEmpty()){
            int[] result = stack.pop();
            int new_idx = result[1]+1;
            
            if (new_idx==numbers.length){
                if (result[0]==target){
                    answer++;
                    
                }
                continue;
            }
            
            stack.push(new int[]{result[0]+numbers[new_idx], new_idx});
            stack.push(new int[]{result[0]-numbers[new_idx], new_idx});
        }
        return answer;
    }
}