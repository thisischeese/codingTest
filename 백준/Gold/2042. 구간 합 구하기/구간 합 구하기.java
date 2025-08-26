import java.io.*; 
import java.util.*; 
import java.math.BigInteger;


public class Main {

	public static long N,M,K,h;
	public static long[] arr; 
	public static long[] segTree; 
	public static StringBuilder sb; 
	
	public static long init(long curr_idx, long start, long end) {
		if(start==end) {return segTree[(int) curr_idx]=arr[(int) start]; }
		
		return segTree[(int) curr_idx] = init(curr_idx*2,start,(start+end)/2)+init(curr_idx*2+1,(start+end)/2+1,end); // 왼 자식 + 오 자식  
	}
	
	// 원본 배열 arr의 curr_num이 변경되는 경우 
	// curr_num이 영향을 끼치는 start~end까지의 구간합을 저장하는 segTree의 curr_idx를 탐색하고
	// diff를 더해줌 
	// start와 end 구간을 변경해가며 탐색하기에 
	// 구간 범위가 curr_num에 해당하지 않는 경우 종료 
	// (start와 end는 curr_num이 영향을 미치는 구간을 찾기 위해 필요한 것임)
	// 루트에서 리프 노드까지 다 내려가야 종료되도록 재귀로 구현하기 
	public static void update(int curr_idx, long start, long curr_num, long end, long diff) {
		
		if(start>curr_num || end<curr_num) {return;}
		
		segTree[curr_idx] += diff; // curr_num이 영향을 미치는 범위에 해당할 때만 해당 트리 노드에 차이 업데이트 
		if(start!=end) {
			// 왼쪽 구간 탐색 후 해당되는 부분 있으면 업데이트
			update(curr_idx*2,start,curr_num,(start+end)/2,diff); 
			// 오른쪽 구간 탐색 후 해당되는 부분 있으면 업데이트
			update(curr_idx*2+1,((start+end)/2)+1,curr_num,end,diff);
		}
		
	}
	
	// start와 end를 가지고 
	// 타겟 curr_idx 찾고 
	// segTree의 curr_idx를 반환하기 
	// 루트 노드에서 시작해서 타겟 노드까지 도달하기 
	public static long getSum(int curr_idx,long start, long end, long tstart, long tend) {
		// 만약 타겟 구간을 벗어나는 경우 종료 
		if(tstart>end || tend<start) {return 0;}
		// 타겟 구간에 해당하는 경우 
		if(tstart<=start && end<=tend) {return segTree[curr_idx];}
		// 일단 갈라져서 내려가는데 만약 구간보다 크면 더 내려가기 
		
		return getSum(curr_idx*2,start,(start+end)/2,tstart,tend)+getSum(curr_idx*2+1,((start+end)/2)+1,end,tstart,tend); 
		
	}

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine()); 
		sb = new StringBuilder(); 
		
		N = Long.parseLong(st.nextToken()); 
		M = Long.parseLong(st.nextToken()); 
		K = Long.parseLong(st.nextToken()); 
		arr = new long[(int) (N+1)]; 
		for(int i=1;i<=N;i++) {
			long num = Long.parseLong(br.readLine()); 
			arr[i] = num; // 1 ~ N 범위 인덱스로 접근 
		}
		// 세그먼트 트리 초기화 
		h = (int)Math.ceil(Math.log(N)/Math.log(2)); 
		segTree = new long[(int)Math.pow(2, h+1)]; 
		init(1,1,N);
		
		for(int i=0;i<M+K;i++) {
			st = new StringTokenizer(br.readLine()); 
			
			int a = Integer.parseInt(st.nextToken()); 
			long b = Long.parseLong(st.nextToken()); 
			long c = Long.parseLong(st.nextToken()); 
			
			if(a==1) {long diff = c-arr[(int) b]; arr[(int) b]=c; update(1,1,b,N,diff); } // 세그먼트 트리 업데이트는 루트 노드부터 리프 노드까지 
			else if(a==2) {sb.append(getSum(1,1,N,b,c)).append("\n"); } // 구간 합 출력하는데 루트 노드에서 탐색을 시작하기 
		}
		
		br.close();
		System.out.println(sb.toString());
	}

}
