import java.io.*;
import java.util.*; 

public class Main {

	
	public static void bt(int cnt, int idx, int N, int M,boolean[]v,int[] temp,int[] arr, StringBuilder sb) {
		int prev = -1; 
		
		if(cnt==M) {for(int t:temp) {sb.append(t).append(" ");} sb.append("\n"); return; }
		for(int i=0;i<arr.length;i++) {
			if(v[i] || prev==arr[i]) {continue;}
			
			prev = arr[i];
			v[i] = true; 
			temp[cnt] = arr[i];
			bt(cnt+1,i+1,N,M,v,temp,arr,sb);
			v[i] = false; 
		}
	}
	
	public static void main(String[] args) throws Exception{

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken()); 
		int[] arr = new int[N]; 
		List<Integer> arr_set = new ArrayList<>();
		int[] temp = new int[M];
		boolean[] v = new boolean[N];


		int prev = -1;

		st = new StringTokenizer(br.readLine());
		for(int i=0;i<N;i++) {arr[i] = Integer.parseInt(st.nextToken());}
		Arrays.sort(arr);
		
		bt(0,0,N,M,v,temp,arr,sb);
		
		br.close();
		System.out.println(sb.toString());
		
	}

}
