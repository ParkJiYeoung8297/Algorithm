// 1) i를 n 진수로 바꾸기 (Integer.toString(n,radix) 사용하면 자동으로 A-F로 바꿔줌)
// 2) StringBuilder에 추가하고 출력하기 (String 이어붙이는거는 객체 새로 할당해야함. StringBuilder를 사용하면 객체 새로 할당안하고 이러붙일 수 있어서 효율적임)
import java.util.*;
class Solution {
    public String solution(int n, int t, int m, int p) {
        StringBuilder sb = new StringBuilder();
        
        for (int i=0;i<t*m;i++){
            String regex=Integer.toString(Integer.valueOf(i),n);
            sb.append(regex.toUpperCase());
        }
        
        String totalString = sb.toString();
        StringBuilder answer = new StringBuilder();
        for (int i=p;i<t*m+p;i=i+m){
            answer.append(totalString.charAt(i-1));
        }
        return answer.toString();
    }
    
}