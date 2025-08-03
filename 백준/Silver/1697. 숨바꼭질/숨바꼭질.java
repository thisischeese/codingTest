import java.io.*; 
import java.util.*; 

public class Main {
		
	public static int bfs(int curr,int target) {
		int answer = Integer.MAX_VALUE; 
		boolean[] visited = new boolean[100001]; 
		Queue<Integer> queue = new LinkedList<>(); 
		Queue<Integer> queue_time = new LinkedList<>(); 

		queue.add(curr);
		queue_time.add(0);
		
		while(!queue.isEmpty()) {
			int node = queue.poll();
			int time = queue_time.poll(); 
			visited[node]=true; 
			
			if(node==target) {
				answer = Math.min(answer, time);
				}
			
			
			int[] next = {node*2,node+1,node-1};
			for(int n: next) {
				if((0<=n & n<=100000) && !visited[n]) {
					queue.add(n);
					queue_time.add(time+1);
				}
			}
			
			
		}
		return answer;
	}
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
		StringTokenizer st = new StringTokenizer(br.readLine()); 
		StringBuilder sb = new StringBuilder();
		
		int N = Integer.parseInt(st.nextToken()); 
		int K = Integer.parseInt(st.nextToken()); 
		
		int answer = bfs(N,K);
		sb.append(answer); 
		
		br.close();
		System.out.println(sb.toString());
	}

}
