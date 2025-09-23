import java.io.*;
import java.util.*;

public class Main {

    static int N, M;
    static char[][] board;
    static int[][] dist;
    static boolean[][][] v;
    static int[] dr = {1,-1,0,0}, dc = {0,0,1,-1};
    static StringBuilder sb = new StringBuilder();

    static void bfs() {
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{0,0,0});
        v[0][0][0] = true;

        while(!q.isEmpty()){
            int[] curr = q.poll();
            int r = curr[0], c = curr[1], broken = curr[2];

            for(int d=0; d<4; d++){
                int nr = r+dr[d], nc = c+dc[d];
                if(nr<0||nc<0||nr>=N||nc>=M) continue;

                if(board[nr][nc]=='1'){ 
                    if(broken==0 && !v[1][nr][nc]){
                        v[1][nr][nc] = true;
                        dist[nr][nc] = dist[r][c] + 1;
                        q.offer(new int[]{nr,nc,1});
                    }
                } else {
                    if(!v[broken][nr][nc]){
                        v[broken][nr][nc] = true;
                        dist[nr][nc] = dist[r][c] + 1;
                        q.offer(new int[]{nr,nc,broken});
                    }
                }

                if(nr==N-1 && nc==M-1){
                    sb.append(dist[nr][nc] + 1);
                    System.out.println(sb.toString());
                    System.exit(0);
                }
            }
        }
        sb.append(-1);
        System.out.println(sb.toString());
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        if(N==1 && M==1){
            System.out.println(1);
            return;
        }

        board = new char[N][M];
        dist = new int[N][M];
        v = new boolean[2][N][M];

        for(int i=0;i<N;i++){
            String s = br.readLine();
            for(int j=0;j<M;j++){
                board[i][j] = s.charAt(j);
            }
        }

        bfs();
    }
}
