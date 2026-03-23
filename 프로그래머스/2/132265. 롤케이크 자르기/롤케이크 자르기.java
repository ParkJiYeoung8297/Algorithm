// 토핑의 개수가 동일해야 한다.
// 처음 시작은 brother가 모두 가졌다고 가정해서 dict로 모든 요소 개수 세기
// 이후 동생이 하나씩 가져가면서, set요소와 dict 요소가 같아지면 answer++;

import java.util.*;
class Solution {
    public int solution(int[] topping) {
        int answer = 0;
        Map<Integer,Integer> brother = new HashMap<>();
        HashSet<Integer> younger = new HashSet<>();
        
        for (int i=0; i<topping.length;i++){
            Integer top=Integer.valueOf(topping[i]);
            brother.put(top,brother.getOrDefault(top,0)+1);
        }
        
        for (int i=topping.length-1;i>=0;i--){
            younger.add(topping[i]);
            brother.put(topping[i],brother.get(topping[i])-1);
            if (brother.get(topping[i])==0){
                brother.remove(topping[i]);
            }
            if (brother.size()==younger.size()){
                answer++;
            }
        }
        return answer;
    }
}