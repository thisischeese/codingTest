import java.io.*; 
import java.util.*; 

public class Main/*BJ_2630*/ {
	
	public static int blue = 0; 
	public static int white = 0; 
	public static int check(int sr,int er, int sc,int ec, int[][] board) {
		int flag = board[sr][sc]; 
		for(int i = sr;i<=er;i++) {
			for(int j = sc;j<=ec;j++) {
				if(board[i][j]!=flag) {return -1;}
			}
		}
		return flag; 
	}
	public static void dc(int sr,int er, int sc,int ec, int[][] board) {
		 if(er==sr) {
			 if (board[sr][sc]==1) {blue++;}
			 else {white++;}
			 return; 
		 }
		 if(check(sr,er,sc,ec,board)==1) {blue++;}
		 else if(check(sr,er,sc,ec,board)==0) {white++;}
		 else { // 4개로 쪼개기 
			 int dist = (er-sr+1)/2; 
			 dc(sr,sr+dist-1,sc,sc+dist-1, board); // 좌상
			 dc(sr+dist,er, sc,sc+dist-1, board); // 우상
			 dc(sr,sr+dist-1,sc+dist, ec, board); // 좌하
			 dc(sr+dist,er, sc+dist, ec, board); // 우하 
			 }
		 
	}
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder(); 
		int N = Integer.parseInt(br.readLine()); 
		int [][] board = new int[N][N]; 
		for(int i = 0;i<N;i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int j =0; j<N;j++) {
				board[i][j] = Integer.parseInt(st.nextToken()); 
			}
		}
		
		dc(0,N-1,0,N-1,board); 
		sb.append(white+"\n"); 
		sb.append(blue); 
		System.out.println(sb.toString());
		br.close();

	}

}
