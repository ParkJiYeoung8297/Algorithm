// 진수 변환하는 방법 - radixChange
// 소수인지 판단하는 방법 - isPrime (제곱근까지만 탐색)
// 제곱 - Math.pow()
// StringBuilder로 String 이어붙이기

// 런타임 에러가 났을 때는, int를 Long으로 바꿔보기 (int 범위 초과라 에러날 수도 있음)

import java.util.*;
class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        
        String radix = radixChange(n,k);
        String[] arr = radix.split("0");

        for (String s:arr){
            if (!s.isBlank() && isPrime(Long.parseLong(s))){
                answer++;
            }
        }
        return answer;
    }
    
    private String radixChange(int num, int radix){
        StringBuilder sb = new StringBuilder();
        while(num!=0){
            sb.append(num%radix);
            num=num/radix; 
        }
        return sb.reverse().toString();
    }
    
    private boolean isPrime(long num){
        if (num==1){
            return false;
        }
        for (int i=2;i<=Math.sqrt(num);i++){
            if (num%i==0){
                return false;
            }
        }
        return true;
    }
    
}