import java.io.*;
import java.util.*;

public class Main {

    static int N, cnt;
    static int[][] board;
    static boolean[][] v;
    static int[] dr = {1,-1,0,0}, dc = {0,0,1,-1};
    static List<Integer> result;
    static StringBuilder sb = new StringBuilder();

    static void dfs(int r,int c){
        v[r][c] = true;
        for(int d=0;d<4;d++){
            int nr = r+dr[d], nc = c+dc[d];
            if(nr>=0 && nc>=0 && nr<N && nc<N && !v[nr][nc] && board[nr][nc]==1){
                cnt++;
                dfs(nr,nc);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        board = new int[N][N];
        v = new boolean[N][N];
        result = new ArrayList<>();

        for(int i=0;i<N;i++){
            String s = br.readLine();
            for(int j=0;j<N;j++){
                board[i][j] = s.charAt(j)-'0';
            }
        }

        for(int r=0;r<N;r++){
            for(int c=0;c<N;c++){
                if(board[r][c]==1 && !v[r][c]){
                    cnt = 1;
                    dfs(r,c);
                    result.add(cnt);
                }
            }
        }

        Collections.sort(result);
        sb.append(result.size()).append("\n");
        for(int r:result) sb.append(r).append("\n");

        System.out.println(sb.toString());
    }
}
