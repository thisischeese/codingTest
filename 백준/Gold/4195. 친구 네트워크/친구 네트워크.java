import java.io.*; 
import java.util.*; 

public class Main {

	public static int F,N,friendCnt; 
	public static Map<String,Integer> hashMap; // 0 base
	public static int[] parents,size; 
	public static StringBuilder sb = new StringBuilder(); 
	
	public static int find(int a) {
		if(parents[a]==a) {return a; }
		return parents[a] = find(parents[a]); 
	}
	
	public static void union(int a, int b) {
		int pa = find(a); 
		int pb = find(b); 
		if(pa!=pb) {
			parents[pb] = pa; 
			size[pa] += size[pb]; 
		}
	}
	
	public static int calFriends(int p) {
		int cnt = 0; 
		for(int temp : parents) {
			if (temp ==p) {cnt++;}
		}
		
		return cnt; 
	}
	
	public static void main(String[] args) throws Exception{

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
		StringTokenizer st; 
		
		F = Integer.parseInt(br.readLine()); 
		for(int t=1;t<=F;t++) {
			N = Integer.parseInt(br.readLine()); 
			hashMap = new HashMap<>(); 
			parents = new int[N*2]; size = new int[N*2];
			for(int i=0;i<N*2;i++) {parents[i] = i; }
			for(int i=0;i<N*2;i++) {size[i] = 1; }
			
			friendCnt = 0; 
			
			for(int i=0;i<N;i++) {
				st = new StringTokenizer(br.readLine()); 
				// 친구 1의 idx 구하기 -> 만약 없다면 friendCnt를 더해서 키:밸 만들어주기 
				String f1 = st.nextToken(); 
				if(!hashMap.containsKey(f1)) {hashMap.put(f1, friendCnt++);}
				// 친구 2의 idx 구하기 -> 만약 없다면 friendCnt를 더해서 키:밸 만들어주기 
				String f2 = st.nextToken(); 
				if(!hashMap.containsKey(f2)) {hashMap.put(f2, friendCnt++);}
				// 친구 1과 친구 2 union
				//System.out.println(hashMap.get(f1));
				//System.out.println(hashMap.get(f2));
				
				union(hashMap.get(f1),hashMap.get(f2)); 
				
				// parents에서 친구1과 친구2의 부모와 같은 부모를 가지는 노드의 개수 카운트하여 sb append
				//int answer = calFriends(find(hashMap.get(f1))); 
				//for(String k : hashMap.keySet()) {sb.append(k).append(" : ").append(hashMap.get(k)).append(" ,"); }
				//for(int p: parents) {sb.append(p).append(" ");}sb.append("\n");
				sb.append(size[find(hashMap.get(f1))]).append("\n"); 
			}
		}
		
		
		br.close();
		System.out.println(sb.toString());
	}

}
