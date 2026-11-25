// stack으로 짝지어 제거하기

import java.util.*;

class Solution
{
    public int solution(String s)
    {
        Stack<String> stack=new Stack<>();
        
        for (String s1 : s.split("")){
            if (!stack.isEmpty() && stack.peek().equals(s1)){
                stack.pop();
            }
            else{
                stack.push(s1);
            }
        }
        
        return stack.isEmpty() ? 1 : 0;
    }
}