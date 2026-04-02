// 포인터를 start와 end로 해서 자른 것을 element라고 할 때, 
// element가 dict에 없으면 start와 end-1 자른거를 출력하고, element는 dict에 추가
import java.util.*;
class Solution {
    public int[] solution(String msg) {
        int[] answer = {};
        List<Integer> ans = new ArrayList<>();
        
        Map<String, Integer> dicts = new HashMap<>();
        String[] alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");
        
        for (int i=0;i<26;i++){
            dicts.put(alpha[i],i+1);
        }
        
        int start=0;
        int end;
        
        while(start<msg.length()){
            String target=""+msg.charAt(start);
            end=start+1;

            while(end<=msg.length() && dicts.containsKey(msg.substring(start, end))){
                target=msg.substring(start,end);
                end++;
            }
            ans.add(dicts.get(target));
            if (end<msg.length()){
                dicts.put(msg.substring(start, end),dicts.size()+1);
            }
            start+=target.length();
        }
    
        answer = new int[ans.size()];
        for (int i = 0;i<ans.size();i++){
            answer[i]=ans.get(i);
        }
        
        return answer;
    }
}