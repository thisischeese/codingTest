import java.io.*; 
import java.util.*; 

public class Main {

	private static int N,M,R;
	private static int[][] arr;
	private static StringBuilder sb = new StringBuilder();
	
	private static void rotate() {
		for(int i=0;i<N/2;i++) {
			if(i>=M/2) {break;}
			Queue<Integer> queue = new ArrayDeque<>();
			// 위 삽입 
			for(int j=i;j<M-i;j++) {queue.add(arr[i][j]);}
			// 오 삽입 
			for(int j=i+1;j<N-i-1;j++) {queue.add(arr[j][M-i-1]);}
			// 하 삽입 
			for(int j=M-i-1;j>=i;j--) {queue.add(arr[N-i-1][j]);}
			// 왼 삽입 
			for(int j=N-i-2;j>i;j--) {queue.add(arr[j][i]);}
			
			//rotate 
			for(int r=0;r<R;r++) {int temp = queue.poll(); queue.add(temp);}
			
			// 위 삽입 
			for(int j=i;j<M-i;j++) {arr[i][j] = queue.poll();}
			// 오 삽입 
			for(int j=i+1;j<N-i-1;j++) {arr[j][M-i-1] = queue.poll();}
			// 하 삽입 
			for(int j=M-i-1;j>=i;j--) {arr[N-i-1][j] = queue.poll();}
			// 왼 삽입 
			for(int j=N-i-2;j>i;j--) {arr[j][i] = queue.poll();}
			
		}
	}
	
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		R = Integer.parseInt(st.nextToken());
		arr = new int[N][M];
		for(int i=0;i<N;i++) {st = new StringTokenizer(br.readLine()); for(int j=0;j<M;j++) {arr[i][j] = Integer.parseInt(st.nextToken());}}
		
		rotate();
		
		for(int i=0;i<N;i++) {for(int j=0;j<M;j++) {sb.append(arr[i][j]).append(" ");} sb.append("\n");}
		
		br.close();
		System.out.println(sb.toString());
	}

}
