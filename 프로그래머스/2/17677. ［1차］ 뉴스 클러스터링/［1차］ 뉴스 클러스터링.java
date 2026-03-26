// 개수 기준, 교집합은 둘 다 있는거 중에 작은값 / 합집합은 다 넣고 둘다 있다면 큰값 (근데 그냥 요소 다 더하고 교집합 개수 빼면 됨!)
import java.util.*;
class Solution {
    public int solution(String str1, String str2) {
        Map<String,Integer> countsOne=countElements(str1);
        Map<String,Integer> countsTwo=countElements(str2);
        int intersection = getIntersection(countsOne, countsTwo);
        int union = getUnion(countsOne, countsTwo)-intersection;
        
        if (union==0){
            return 65536;
        }
        
        return (int)(((double)intersection/union)*65536);
    }
    
    private Map<String,Integer> countElements(String str){
        Map<String,Integer> counts = new HashMap<>();
        for (int i=0;i<str.length()-1;i++){
            String element = str.substring(i,i+2).toLowerCase();
            if (isString(element)){
                counts.put(element,counts.getOrDefault(element,0)+1);
            }
        }
        return counts;
    }
    
    private boolean isString(String s){
        return Character.isLetter(s.charAt(0)) && Character.isLetter(s.charAt(1));
    }
    
    private int getIntersection(Map<String,Integer> countsOne, Map<String,Integer> countsTwo){
        int total = 0;
        for(String key : countsOne.keySet()){
            if (countsTwo.containsKey(key)){
                total+=Math.min(countsOne.get(key),countsTwo.get(key));
            }
        }
        return total;
    }
    
    private int getUnion(Map<String,Integer> countsOne, Map<String,Integer> countsTwo){
        int total = 0;
        for (Integer i: countsOne.values()){
            total+=i;
        }
        for (Integer i: countsTwo.values()){
            total+=i;
        }
        return total;
    }
    
}