import java.io.*; 
import java.util.*; 

// MST 2개 만들기 
// 간선 수가 10^6 정도임 
// MST를 하나 만들고 -> MST에서 끊어도 되는 가장 큰 경로를 찾아서 빼주면 남은 길 유지비 합의 최솟값을 구할 수 있음 
// 궁금한 점... MST는 쪼개도 MST인가??? 


public class Main {

	public static int N,M,total,maxWeight,cntEdge;
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
		return find(parents[a]);
	}
// 1. 가장 작은 간선 찾기 
// 2. 해당 간선으로 인해 사이클이 발생한다면 간선 무시 / 아니라면 
	public static void kruskal() {
		
		while(!pq.isEmpty() && cntEdge<N-1) {
			int[] curr = pq.poll(); 
			// 만약 루트 노드가 같다면 사이클이 발생한다는 뜻 -> 처음으로 돌 때는 모두가 노드가 다를 텐데 뭐 어떻게 처리하는겨? 
			// 아 간선 시작과 끝이니까 
			int pa = find(curr[0]); 
			int pb = find(curr[1]);
			if(pa==pb) {continue;}
			
			union(curr[0],curr[1]); 
			
			maxWeight = Math.max(maxWeight, curr[2]); 
			total += curr[2]; 
			cntEdge++; 
		}
		
		
	}
	
	
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		pq = new PriorityQueue<>((o1,o2) -> o1[2]-o2[2]); // 가중치 기준 오름차순 정렬하기 
		
		st = new StringTokenizer(br.readLine()); 
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());	
		
		cntEdge = 0;
		total = 0;
		maxWeight = -1;
		
		parents = new int[N+1]; // 0은 사용 x
		for(int i=1;i<N+1;i++) {parents[i] =i;} // 각자 자기 자신이 루트 노드 : 고립 
		
		for(int i=0;i<M;i++) {
			st = new StringTokenizer(br.readLine()); 
			int a = Integer.parseInt(st.nextToken()); // 시작 노드 
			int b = Integer.parseInt(st.nextToken()); // 끝나는 노드 
			int c = Integer.parseInt(st.nextToken()); // 가중치 
			
			pq.add(new int[] {a,b,c}); // pq에 모든 간선 정보 넣어두기 
		}
		
		kruskal(); 
		sb.append(total-maxWeight); 
		
		br.close();
		System.out.println(sb.toString());
	}

}
