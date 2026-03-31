// heap을 이용하면 가장 작은 요소를 O(1)로 꺼낼 수 있다.
// PriorityQueue는 최소 요소가 default이고, poll()해서 꺼낸다.
// 값 조회만 할떄는 peek() 사용하기!
import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        int scov=0;
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        for (int s : scoville){
            minHeap.add(s);
        }
        
        while (minHeap.peek()<K){
            if (minHeap.size()<2){
                return -1;
            }
            int min = minHeap.poll();
            int secondMin = minHeap.poll();
            scov=min+secondMin*2;
            minHeap.add(scov);
            
            answer++;
        }
        return answer;
    }
}