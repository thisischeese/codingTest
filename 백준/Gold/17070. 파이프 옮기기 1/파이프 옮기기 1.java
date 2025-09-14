import java.util.*; 
import java.io.*; 

public class Main {

	public static int N,answer,nr1,nc1,nr2,nc2;
	public static int wr1,wr2,wc1,wc2;
	public static int[][] arr; 
	public static StringBuilder sb = new StringBuilder(); 
	
	public static boolean checkWall(int r, int c) {
		
		wr1 = r; wc1 = c-1; 
		wr2 = r-1; wc2 = c; 
		if(arr[r][c]==0 && arr[wr1][wc1]==0 && arr[wr2][wc2]==0) {
			return true; 
		}
		
		
		return false; 
	}
	
	public static void dfs(int r1, int c1, int r2, int c2) {
		
		if(r2==N-1 && c2==N-1) {answer ++; return; }
		
		// 가로일 경우 : 같은 행 위에 위치함  
		if(r1==r2) {
			// 가로 -> 가로 
			nr1 = r1; nc1 = c1+1; nr2 = r2; nc2 = c2+1;
			if(0<=nr1 && nr1<N && 0<=nc1 && nc1<N && arr[nr1][nc1]==0 && 0<=nr2 && nr2<N && 0<=nc2 && nc2<N && arr[nr2][nc2]==0) {dfs(nr1, nc1, nr2, nc2); }
			// 가로 -> 대각선 
			nr1 = r1; nc1 = c1+1; nr2 = r2+1; nc2 = c2+1;
			if(0<=nr1 && nr1<N && 0<=nc1 && nc1<N && arr[nr1][nc1]==0 && 0<=nr2 && nr2<N && 0<=nc2 && nc2<N && checkWall(nr2,nc2)) {dfs(nr1, nc1, nr2, nc2); }
		}
		// 세로일 경우 : 같은 열 위에 위치함 
		else if(c1==c2) {
			// 세로 -> 세로 
			nr1 = r1+1; nc1 = c1; nr2 = r2+1; nc2 = c2;
			if(0<=nr1 && nr1<N && 0<=nc1 && nc1<N && arr[nr1][nc1]==0 && 0<=nr2 && nr2<N && 0<=nc2 && nc2<N && arr[nr2][nc2]==0) {dfs(nr1, nc1, nr2, nc2); }
			// 세로 -> 대각선 
			nr1 = r1+1; nc1 = c1; nr2 = r2+1; nc2 = c2+1;
			if(0<=nr1 && nr1<N && 0<=nc1 && nc1<N && arr[nr1][nc1]==0 && 0<=nr2 && nr2<N && 0<=nc2 && nc2<N && checkWall(nr2,nc2)) {dfs(nr1, nc1, nr2, nc2); }
		}
		// 대각선일 경우 
		else if (r1+1==r2 && c1+1==c2) {
			// 대각선 -> 가로 
			nr1 = r1+1; nc1 = c1+1; nr2 = r2; nc2 = c2+1;
			if(0<=nr1 && nr1<N && 0<=nc1 && nc1<N && arr[nr1][nc1]==0 && 0<=nr2 && nr2<N && 0<=nc2 && nc2<N && arr[nr2][nc2]==0) {dfs(nr1, nc1, nr2, nc2); }
			// 대각선 -> 대각선 
			nr1 = r1+1; nc1 = c1+1; nr2 = r2+1; nc2 = c2+1;
			if(0<=nr1 && nr1<N && 0<=nc1 && nc1<N && arr[nr1][nc1]==0 && 0<=nr2 && nr2<N && 0<=nc2 && nc2<N && checkWall(nr2,nc2)) {dfs(nr1, nc1, nr2, nc2); }
			// 대각선 -> 세로 
			nr1 = r1+1; nc1 = c1+1; nr2 = r2+1; nc2 = c2;
			if(0<=nr1 && nr1<N && 0<=nc1 && nc1<N && arr[nr1][nc1]==0 && 0<=nr2 && nr2<N && 0<=nc2 && nc2<N && arr[nr2][nc2]==0) {dfs(nr1, nc1, nr2, nc2); }
		}
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
		StringTokenizer st; 
		
		answer = 0; 
		
		N = Integer.parseInt(br.readLine()); 
		arr = new int[N][N];
		
		for(int i=0;i<N;i++) {
			st = new StringTokenizer(br.readLine()); 
			for(int j=0;j<N;j++) {
				arr[i][j] = Integer.parseInt(st.nextToken()); 
			}
		}
		br.close();
		dfs(0, 0, 0, 1);
		sb.append(answer); 
		System.out.println(sb.toString());

	}

}

// 방법의 수는 10^6 이하 
// 10^8>10^6