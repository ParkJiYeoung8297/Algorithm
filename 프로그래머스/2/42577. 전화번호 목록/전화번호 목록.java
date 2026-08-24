// 사전식 정렬하면 된다. 사전상 순서에서 가장 가까운 문자가 뒤에 올거니까.
// 뒤에꺼가 앞에꺼로 시작하는지만 체크하면 됨
import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        Arrays.sort(phone_book);
        for(int i = 0;i<phone_book.length-1; i++){
            if (phone_book[i+1].startsWith(phone_book[i])){
                return false;
            }
        }
        return true;
    }
}