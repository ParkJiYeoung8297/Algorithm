// 그룹을 만들고, 그룹 2개의 상자 수 곱이 큰게 최대 점수
import java.util.*;
class Solution {
    public int solution(int[] cards) {
        int[] visited=new int[cards.length];
        ArrayList<Integer> candidate = new ArrayList<>();
        
        for (int i=0;i<cards.length;i++){
            int idx=i;
            int size=0;
            while(visited[idx]!=1){
                size++;
                visited[idx]=1;
                idx=cards[idx]-1;
            }
            candidate.add(size);
        }
        
        if (candidate.size()<2){
            return 0;
        }
        
        Collections.sort(candidate, Collections.reverseOrder());
        return candidate.get(0)*candidate.get(1);
    }
}