// [투포인터 문제]
// 가장 무거운 사람과 가장 가벼운 사람을 같이 태운다. (물론 무게가 가능할 때)
// 오름차순 정렬 : Arrays.sort(배열_변수명)
// 내림차순 정렬 : Arrays.sort(배열_변수명,Comparator.reverseOrder()) 인데 기본형 int[]는 불가능, Integer[]로 사용해야함
import java.util.*;
class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        Arrays.sort(people);
        
        int p1=0;
        int p2=people.length-1;
        
        while(p1<=p2){
            if (people[p2]+people[p1]<=limit){
                p1++;
            }
            answer++;
            p2--;
        }
        return answer;
    }
}