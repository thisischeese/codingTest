import java.io.*; 
import java.util.*; 

public class Main {

	public static void dfs(int curr,boolean[] visited, ArrayList<Integer>[] matrix) {
		if(visited[curr]) {return;} 
		
		visited[curr] = true; 
		if(matrix[curr].size()==0) {return;}
		for(int node : matrix[curr]) {
			if (!visited[node]) {
				dfs(node,visited,matrix);}
		}
		
	}
	
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
		StringBuilder sb = new StringBuilder(); 
		StringTokenizer st; 
		
		st = new StringTokenizer(br.readLine()); 
		int N = Integer.parseInt(st.nextToken()); 
		int M = Integer.parseInt(st.nextToken());
		
		int cnt = 0; 
		boolean[] visited = new boolean[N+1]; 
		
		// 인접 행렬 // 배열[]를 ArrayList로 선언함 
		ArrayList<Integer>[] matrix = new ArrayList[N+1]; 
		for(int i=0;i<N+1;i++) {
			matrix[i] = new ArrayList<Integer>(); 
		}
		
		for(int i=0;i<M;i++) {
			st = new StringTokenizer(br.readLine()); 
			int u = Integer.parseInt(st.nextToken()); 
			int v = Integer.parseInt(st.nextToken());
			matrix[u].add(v); 
			matrix[v].add(u); 
		}
		for(int i=1;i<N+1;i++) {
			if(!visited[i]) {dfs(i,visited,matrix); cnt+=1;}
			}
		br.close();
		sb.append(cnt);
		System.out.println(sb.toString());
	}

}
