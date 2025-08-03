import java.io.*; 
import java.util.*; 

public class Main/*BJ_1697*/ {
		
	public static int bfs(int curr,int target) {
		boolean[] visited = new boolean[100001]; 
		/*
		// 불필요하게 2개의 큐를 사용할 필요가 없음 
		Queue<Integer> queue = new LinkedList<>(); 
		Queue<Integer> queue_time = new LinkedList<>(); 
		 */ 
		// 하나의 큐에서 Pair로 위치와 시간을 같이 관리하기 
		Queue<int[]> queue = new LinkedList<>(); 
		queue.add(new int[] {curr,0}); 
		
		while(!queue.isEmpty()) {
			int[] temp = queue.poll(); 
			int node = temp[0]; 
			int time = temp[1];
			
			if(node==target) {
				return time;
				}
			
			int[] next = {node*2,node+1,node-1};
			for(int n: next) {
				if(0<=n && n<=100000 && !visited[n]) {
					visited[node]=true; 
					queue.add(new int[] {n,time+1});
				}
			}
			
			
		}
		return -1;
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
