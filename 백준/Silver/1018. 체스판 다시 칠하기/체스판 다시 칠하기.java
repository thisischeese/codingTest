import java.io.*; 
import java.util.*; 

public class Main {

	public static int N,M,answer; 
	public static char[][] arr, chess1,chess2;
	public static StringBuilder sb = new StringBuilder(); 
	
	// 보드 초기화 
	public static void init() {
		for(int i=0;i<8;i++) {
			for(int j=0;j<8;j++) {
				if((i%2==0 && j%2==0) || (i%2==1 && j%2==1)) {chess1[i][j] = 'W';chess2[i][j] = 'B';}
				else if((i%2==0 && j%2==1) || (i%2==1 && j%2==0)) {chess1[i][j] = 'B';chess2[i][j] = 'W';}
			}
		}
		
	}
	
	public static int check(int sr, int sc) {
		
		int total1 = 0,total2=0; 
		for(int dr=0;dr<8;dr++) {
			for(int dc =0;dc<8;dc++) {
				if(arr[sr+dr][sc+dc]!=chess1[dr][dc]) {total1++;}
				if(arr[sr+dr][sc+dc]!=chess2[dr][dc]) {total2++;}
			}
		}
			
			
		return Math.min(total1, total2); 
	}
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
		StringTokenizer st; 
		
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken()); 
		M = Integer.parseInt(st.nextToken()); 
		answer = Integer.MAX_VALUE; 
		arr = new char[N][M]; 
		chess1 = new char[8][8]; chess2 = new char[8][8]; 


		for(int i=0;i<N;i++) {
			String s = br.readLine(); 
			for(int j=0;j<M;j++) {
				arr[i][j] = s.charAt(j); 
			}
		}
		init(); 
		
		for(int sr=0;sr<=N-8;sr++) {
			for(int sc=0;sc<=M-8;sc++) {
				int temp = check(sr,sc);
				//sb.append(temp).append("\n"); 
				answer = Math.min(answer,temp); 
			}
		}
		sb.append(answer); 
		br.close();
		System.out.println(sb.toString());
	}

}
