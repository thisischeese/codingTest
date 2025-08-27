import java.io.*; 
import java.util.*; 


public class Main {

	public static int N,M,total,cntEdge; 
	public static int[] parents; 
	public static PriorityQueue<int[]> pq;
	public static StringBuilder sb = new StringBuilder();
	
	
	public static void union(int a, int b) {
		int pa = find(a); 
		int pb = find(b); 
		
		if(pa<pb) {parents[pb] = pa;}
		else {parents[pa] = pb;}
	}
	
	public static int find(int a) {
		if(parents[a]==a) {return a;}
		
		return parents[a]=find(parents[a]); 
	}
	
	public static void kruskal() {
		
		while(!pq.isEmpty() && cntEdge<N-1) {
			
			int[] curr = pq.poll(); 
			// 사이클이 존재한다면 종료하기 
			if(find(curr[0])==find(curr[1])) {continue;}
			
			union(curr[0],curr[1]); 
			cntEdge++; 
			total += curr[2]; 
			
			
		}
		
	}
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
		StringTokenizer st;
		
		pq = new PriorityQueue<>((o1,o2)->o1[2]-o2[2]); 
		
		N = Integer.parseInt(br.readLine());
		M = Integer.parseInt(br.readLine());
		
		parents = new int[N+1];// 0 x
		for(int i=1;i<=N;i++) {parents[i]=i;}
		
		total = 0; 
		cntEdge = 0; 
		
		// 10^5 ok 
		for(int i=0;i<M;i++) {
			st = new StringTokenizer(br.readLine()); 
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			
			pq.add(new int[] {a,b,c}); 
		}
		
		kruskal(); 
		sb.append(total); 
		
		br.close();
		System.out.println(sb.toString());
	}

}
