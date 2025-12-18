import java.util.ArrayList;
import java.util.stream.Collectors;
class Solution {
    public int[] solution(int[] arr, int divisor) {

        ArrayList<Integer> cand=new ArrayList<>();
        for (int i:arr){
            if (i%divisor==0){
                cand.add(i);
            }
        }
        
        if (cand.size()==0){
            return new int[]{-1};
        }
        
        int[] answer = cand.stream()
            .sorted()
            .mapToInt(Integer::intValue)
            .toArray();
        
        return answer;
    }
}