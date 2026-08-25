// 힙으로 pop 두 번 하고, 1번 넣음
// 처음 pop 했을 때 값이 k 이상이면 끝
import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        
        for (int i = 0; i< scoville.length;i++){
            heap.add(scoville[i]);
        }
        
        while(heap.size()>1){
            int a = heap.poll();
            if (a >= K){
                return answer;
            }
            int b = heap.poll();
            heap.add(a+b*2);
            answer++;
        }
        int a=heap.poll();
        
        if (a>=K){
            return answer;
        }
        
        return -1;
    }
}