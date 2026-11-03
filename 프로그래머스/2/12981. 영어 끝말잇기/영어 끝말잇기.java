import java.util.*;
class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = {0,0};
        HashSet<String> set = new HashSet<>();

        String preLetter = getLastLetter(words[0]);
        set.add(words[0]);
        
        for (int i = 1; i<words.length; i++){
            if (set.contains(words[i]) || !words[i].startsWith(preLetter)){
                return new int[]{i%n+1, i/n+1};
            }
            set.add(words[i]);
            preLetter = getLastLetter(words[i]);
        }
        return answer;
    }
    
    String getLastLetter(String word){
        String[] s = word.split("");
        return s[s.length-1];
    }       
}