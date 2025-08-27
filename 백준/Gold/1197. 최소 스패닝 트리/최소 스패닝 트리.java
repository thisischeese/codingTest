import java.io.*; 
import java.util.*; 
// 하나의 그래프에는 여러 개의 신장트리가 존재할 수 있다
// 여러 개의 신장 트리 중 값의 합이 최소인 최소 비용 신장트리 MST를 구해보자 
// -> 크루스칼 or 프림 

// MST의 가중치 합을 구하는 문제 
// 가중치는 음수 가능 -> 크루스칼 ?

// 간선이 많으면 프림 O(ElogV)
//    1. 임의의 간선 하나 선택
//    2. 선택한 간선 정점과 인접한 정점 중 최소 가중치 간선으로 연결된 정점과 연결
//    3. 모든 정점이 선택되면 완료 
//    
// 간선이 적으면 크루스칼 : O(ElogE)
//    1. 모든 간선을 가중치 기준 오름차순 정렬 
//    2. 최소 가중치 간선부터 순차적으로 선택하되 싸이클 형성되면 선택 x(find : O(1))
//                                    싸이클이 형성되지 않으면 선택 
//    3. 만약 간선 N-1개가 선택된다면 완료하기 

public class Main {

	public static int V,E,totalSum,cntEdge;
	// public static List<int[]>[] arr; // 인접 리스트
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
		
		return parents[a]= find(parents[a]); 
	}
	
	public static void kruskal() {
		// 2. 간선 개수 V-1될 때까지 반복 ->
		while(!pq.isEmpty() && cntEdge<V-1) {
			// 2-1. poll하고 find로 부모 검사 
			int[] curr = pq.poll();
			int p0 = find(curr[0]); 
			int p1 = find(curr[1]);
			// 2-1-1. 부모가 같으면 선택 x
			if(p0==p1) {continue;}
			// 2-1-2. 부모가 다르면 선택하고 total update && 간선 개수 update && union 
			union(curr[0],curr[1]); 
			totalSum += curr[2]; 
			cntEdge++; 

		}
		
		
	}
	
	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
		StringTokenizer st = new StringTokenizer(br.readLine()); 
		
		V = Integer.parseInt(st.nextToken()); 
		E = Integer.parseInt(st.nextToken()); 
		parents = new int[V+1];
		for(int i=0;i<V+1;i++) {parents[i] = i; }
		totalSum = 0; 
		cntEdge = 0; 
		
		pq = new PriorityQueue<>((a,b)->a[2]-b[2]); // 가중치 기준으로 정렬하기 
		
		for(int i=0;i<E;i++) {
			st = new StringTokenizer(br.readLine()); 
			int a = Integer.parseInt(st.nextToken()); // a번 정점 
			int b = Integer.parseInt(st.nextToken()); // b번 정점 
			int c = Integer.parseInt(st.nextToken()); // c 가중치 
			// pq
			// 1. 간선 가중치 순으로 정렬하기 (pq에 한 번에 삽입)
			pq.add(new int[] {a,b,c}); // start V, end V, Weights
	}
		
		kruskal(); 
		sb.append(totalSum); 
		
		br.close();
		System.out.println(sb.toString());
	}
}


/*
 * 1. 간선 가중치 순으로 정렬하기 (pq에 한 번에 삽입)
 * 2. 간선 개수 N-1될 때까지 반복 ->
 * 	2-1. poll하고 find로 부모 검사
 * 		2-1-1. 부모가 같으면 선택 x
 *      2-1-2. 부모가 다르면 선택하고 total update && 간선 개수 update && union 
 * */