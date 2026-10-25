// BFS로 풀어야 최단 거리 보장
// 각 노드까지의 최단 거리를 비교했을 때 가장 먼 노드
import java.util.*;
class Solution {
    static HashMap<Integer, ArrayList<Integer>> dict = new HashMap<>();
    static int[] visited;
    
    public int solution(int n, int[][] edge) {
        int answer = 0;
        visited = new int[n+1];
        Arrays.fill(visited, -1);

        for (int[] e : edge){
            dict.computeIfAbsent(e[0], k -> new ArrayList<Integer>()).add(e[1]);
            dict.computeIfAbsent(e[1], k-> new ArrayList<Integer>()).add(e[0]);
        }
        
        ArrayDeque<int[]> queue = new ArrayDeque<>();
        queue.addLast(new int[]{1, 0});    // 현재 위치, 간 거리
        visited[1]=1;
        
        int maxDistance=0;
            
        
        while(!queue.isEmpty()){
            int[] result = queue.removeFirst();
            int current = result[0];
            int distance = result[1];
            
            for (int next : dict.getOrDefault(current, new ArrayList<>())){
                if (visited[next] != -1){
                    continue;
                }
                
                visited[next]=distance + 1;
                queue.addLast(new int[]{next, visited[next]});
                maxDistance = Math.max(maxDistance, visited[next]);
            }
            
        }
        
        for(int i : visited){
            if (i == maxDistance){
                answer++;
            }
        }
        
        return answer;
    }
}