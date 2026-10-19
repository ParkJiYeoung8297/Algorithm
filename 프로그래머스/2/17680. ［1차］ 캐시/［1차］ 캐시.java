// 자바에서 deque은 중간 값 제거도 가능함 
import java.util.*;
class Solution {
    static Deque<String> deque = new ArrayDeque<>();
    
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        if(cacheSize==0){
            return cities.length*5;
        }
        
        for (String city:cities){
            String lowerCaseCity = city.toLowerCase();
            if(isHit(lowerCaseCity)){
                answer++;
                deque.remove(lowerCaseCity);
                deque.add(lowerCaseCity);
            } else{
                answer+=5;
                
                if(isFullCache(cacheSize)){
                    deque.removeFirst();
                }
                deque.addLast(lowerCaseCity);
            }
        }
        return answer;
    }
    
    boolean isHit(String s){
        return deque.contains(s);
    }
    
    boolean isFullCache(int cacheSize){
        return deque.size()==cacheSize;
    }
}