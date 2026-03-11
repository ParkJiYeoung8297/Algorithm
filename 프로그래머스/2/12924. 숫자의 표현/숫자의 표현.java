// m, m+1, m+2 와 같이 1씩 증가하는 수열이다.
// m, m+1 → 2*m+(0+1)
// m, m+1, m+2 → 3*m+(0+1+2)
// 이 아이디어가 잘 안와닿는듯 (기억하기)

class Solution {
    public int solution(int n) {
        int answer = 0;
        
        int m=1;
        int s=0;
        while (n-s>0){
            if ((n-s)%m==0){
                answer++;
            }
            s+=m;
            m++;
        }
        return answer;
    }
}