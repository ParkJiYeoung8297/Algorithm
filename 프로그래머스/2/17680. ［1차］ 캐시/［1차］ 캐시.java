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
                
                Stack<String> stack = new Stack<>();
                while(!deque.isEmpty()){
                    String removed = deque.removeFirst();
                    if(removed.equals(lowerCaseCity)){
                        deque.add(lowerCaseCity);
                        break;
                    }
                    stack.add(removed);
                }
                
                while(!stack.isEmpty()){
                    deque.addFirst(stack.pop());
                }
                
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