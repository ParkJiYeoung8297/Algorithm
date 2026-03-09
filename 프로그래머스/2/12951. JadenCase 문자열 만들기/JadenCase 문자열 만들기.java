// s.split(" ",-1)을 하면 빈문자열까지 포함하라는 의미이다. 
// String_변수명.toLowerCase(), String_변수명.toUpperCase()

import java.util.*;
class Solution {
    public String solution(String s) {
        String answer = "";
        String[] sentences = s.split(" ",-1);
        List<String> candidate = new ArrayList<>();
        
        for (String sent : sentences){
            if (sent.isBlank()){
                candidate.add(sent);
                continue;
            }
            String lowerSent = sent.toLowerCase();
            candidate.add(lowerSent.substring(0,1).toUpperCase()+lowerSent.substring(1));
        }
        
        answer = String.join(" ",candidate);

        return answer;
    }
}