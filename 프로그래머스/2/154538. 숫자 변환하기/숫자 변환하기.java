// BFS 문제 (3가지 방법 중 선택)
// 3 곱하기 → 2 곱하기 → n 더하기 순으로 연산을 줄여준다.
import java.util.*;
class Solution {
    public int solution(int x, int y, int n) {
        if (x==y) { // 엣지 케이스
            return 0;
        }
        
        Deque<int[]> deq = new ArrayDeque<>();

        deq.add(getArr(three(y), 1));
        deq.add(getArr(two(y), 1));
        deq.add(getArr(one(y,n), 1));
        
        while (!deq.isEmpty()){
            int[] tuple=deq.pollFirst();  // 현재 값, 연산 횟수
            if (tuple[0]<=0){
                continue;
            }
            if (tuple[0]==x){
                return tuple[1];
            }
            
            deq.add(getArr(three(tuple[0]), tuple[1]+1));
            deq.add(getArr(two(tuple[0]), tuple[1]+1));
            deq.add(getArr(one(tuple[0],n), tuple[1]+1));
        }
        
        return -1;
    }
    
    private int[] getArr(int a, int b){
        int[] tuple={a,b};
        return tuple;
    }
    
    private int three(int i){
        if (i%3==0){
            return i/3;
        }
        return 0;
    }
    
    private int two(int i){
        if (i%2==0){
            return i/2;
        }
        return 0;
    }
    
    private int one(int i, int n){
        return i-n;
    }
}