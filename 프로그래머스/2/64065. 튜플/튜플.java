// 개수를 하나씩 세고, 개수가 제일 많은 거 순서대로 출력
import java.util.*;
class Solution {
    public int[] solution(String s) {
        s=s.replace("{","");
        s=s.replace("}","");
        String[] elements=s.split(",");
        
        Map<String,Integer> counts = new HashMap<>();
        for (String e:elements){
            counts.put(e,counts.getOrDefault(e,0)+1);
        }
        
        int[] answer = new int[counts.size()];
        for (String e:counts.keySet()){
            answer[counts.size()-counts.get(e)]=Integer.parseInt(e);
        }
        return answer;
    }
}