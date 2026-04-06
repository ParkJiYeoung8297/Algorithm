// 보조 컨테이너는 stack
// 보조 컨테이너 맨뒤를 기준으로만 비교함 (어처피 메인꺼 보조로 넘어가니까)
import java.util.*;
class Solution {
    public int solution(int[] order) {
        int answer = 0;
        int[] boxes = new int[order.length];
        Deque<Integer> container = new ArrayDeque<>();
        Deque<Integer> subContainer = new ArrayDeque<>();
        
        for (int i=1;i<=order.length;i++){
            container.add(i);
            boxes[i-1]=i;
        }
        
        for (int i=0;i<order.length;i++){
            boolean isAdded= false;
            int target = boxes[order[i]-1];
            while(container.size()>0){
                if (subContainer.size()==0){
                    subContainer.add(container.poll());
                }
                if (subContainer.peekLast()==target){
                    subContainer.pollLast();
                    answer++;
                    isAdded=true;
                    break;
                }
                subContainer.add(container.poll());
            }
            
            if (subContainer.size()!=0 && subContainer.peekLast()==target){
                subContainer.pollLast();
                answer++;
                isAdded=true;
            }
            
            if (!isAdded){
                break;
            }
        }
        return answer;
    }
}