// 최대 약수를 구하는 것 (본인제외)
// 10,000,000까지의 숫자라는 조건 주목
class Solution {
    public int[] solution(long begin, long end) {
        int[] answer = new int[(int) (end-begin)+1];
        int idx=0;
        
        while(begin<=end){
            answer[idx]=(int) findBiggestDiviser(begin);
            begin++;
            idx++;
        }
           
        return answer;
    }
    
    public long findBiggestDiviser(long num){    
        if (num==1){
            return 0L;
        }
    
        long biggest=1L;
        for (long i = 2;i*i<=num;i++){
            if (num%i==0){
                long pair = num/i;
                if (pair<=10_000_000){
                    return pair;
                }
                biggest=i;
            }
        }
        return biggest; 
    }
}