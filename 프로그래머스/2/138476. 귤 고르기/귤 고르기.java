// [그리디]
// 개수를 세고, 종류가 많은거 우선적으로 넣는다.
import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        Map<Integer,Integer> count = new HashMap();
        for (int tan : tangerine){
            if (!count.containsKey(tan)){
                count.put(tan,0);
            }
            count.put(tan,count.get(tan)+1);
        }
        
        List<Integer> countValue = new ArrayList<>(count.values());
        Collections.sort(countValue, Comparator.reverseOrder());
        
        for (int i=0; i<countValue.size(); i++){
            k-=countValue.get(i);
            if (k<=0){
                answer=i+1;
                break;
            }
        }
        return answer;
    }
}