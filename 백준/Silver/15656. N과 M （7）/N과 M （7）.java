import java.io.*;
import java.util.*; 

public class Main {

	public static void bt(int cnt, int idx, int N, int M, int[] temp, int[] arr, StringBuilder sb) {
		if(cnt==M) {
			for(int t: temp) {sb.append(t).append(" ");} sb.append("\n");
			return; 
		}
		for(int i=0;i<N;i++) {
			temp[cnt]= arr[i]; 
			bt(cnt+1,i+1,N,M,temp,arr,sb);
		}
		
	}
	
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		StringTokenizer st = new StringTokenizer(br.readLine());;
		int N = Integer.parseInt(st.nextToken()); 
		int M = Integer.parseInt(st.nextToken()); 
		int[] arr = new int[N]; 
		int[] temp = new int[M]; 
		
		st = new StringTokenizer(br.readLine());
		for(int i=0;i<N;i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(arr);
		bt(0,0,N,M,temp,arr,sb);
		br.close();
		System.out.println(sb.toString());

	}

}
