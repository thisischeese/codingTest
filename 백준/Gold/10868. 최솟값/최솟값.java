import java.io.*; 
import java.util.*; 

// 세그먼트 트리의 각 노드(start는 i, end는 j )에는 
// i번부터 j번까지의 값 중 최솟값만이 저장된다. 


public class Main {

	public static StringBuilder sb = new StringBuilder(); 
	
	public static long N,M,h;
	public static long[] arr; 
	public static long[] tree; 
	// 최솟값만을 저장하는 세그먼트 트리 
	public static long init(long curr_idx,long start, long end) {
		if(start==end) {return tree[(int) curr_idx]=arr[(int) start]; }
		
		return tree[(int)curr_idx] = Math.min(init(curr_idx*2,start,(start+end)/2),init(curr_idx*2+1,(start+end)/2+1,end)); 
	}
	public static long getMin(long curr_idx, long start, long end, long tstart, long tend) {
		if(tend<start || end<tstart) {return Long.MAX_VALUE;}
		
		if(tstart<=start && end<=tend) {return tree[(int) curr_idx];}
		
		return Math.min(getMin(curr_idx*2, start, (start+end)/2, tstart, tend),getMin(curr_idx*2+1, (start+end)/2+1,end, tstart, tend));
	}
	
	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
		StringTokenizer st = new StringTokenizer(br.readLine()); 
		
		// 1 ~ 10^6 
		N = Integer.parseInt(st.nextToken()); 
		M = Integer.parseInt(st.nextToken()); 		
		arr = new long[(int) N+1]; 
		
		for(int i=1;i<=N;i++) {
			// 1 ~ 10^9 
			long temp = Long.parseLong(br.readLine()); 
			arr[i] = temp; 
		}
		
		// init -> 트리 초기화 루트 노드부터 
		h = (long)Math.ceil(Math.log(N)/Math.log(2)); 
		tree = new long[(int) Math.pow(2,h+1)]; 
		init(1,1,N); // 루트 노드는 1부터 시작 
		
		
		
		for(int i=0;i<M;i++) {
			st = new StringTokenizer(br.readLine()); 
			long a = Long.parseLong(st.nextToken()); // start
			long b = Long.parseLong(st.nextToken()); // end 
			// start~end 사이의 최솟값을 getNode로 가져오기 
			sb.append(getMin(1,1,N,a,b)).append("\n"); 
		}
		
		br.close();
		System.out.println(sb.toString());
		
	}

}
