// 'A', 'E', 'I', 'O', 'U'

import java.util.*;
class Solution {
    public int solution(String word) {
        int answer = 0;
        Map<Character, Integer> map = new HashMap<>();
        map.put('A', 1);
        map.put('E', 2);
        map.put('I', 3);
        map.put('O', 4);
        map.put('U', 5);
        
        int[] scale = {780, 155, 30, 5, 0};

        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            answer += scale[i] * (map.get(c) - 1) + map.get(c);
        }
            
return answer;
    }
}