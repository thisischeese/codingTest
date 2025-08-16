import java.io.*; 
import java.util.*; 


public class Main {
	
	private static int N,M;
	private static int[] arr,temp;
	private static StringBuilder sb = new StringBuilder();

	private static void bt(int cnt,int idx) {
		if(cnt==M) {for(int t:temp) {sb.append(t).append(" ");} sb.append("\n"); return;}
		int prev = -1;
		for(int i=idx;i<N;i++) {
			if(i==idx) {prev = arr[idx];}
			else if(prev==arr[i]) {continue;}
			temp[cnt] = arr[i];
			bt(cnt+1,i+1);
			prev = arr[i];
		}
		
	}
	
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		arr =  new int[N];
		temp = new int[M];
		st = new StringTokenizer(br.readLine());
		for(int i=0;i<N;i++) {arr[i] = Integer.parseInt(st.nextToken());}
		Arrays.sort(arr);
		bt(0,0);
		
		br.close();
		System.out.println(sb.toString());
	}

}
