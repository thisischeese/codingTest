import java.io.*;
import java.util.*;


// 가중치 1인 그래프에서 타겟까지의 최단거리를 찾는 문제라고 봐도 무방함 
// 나이트의 이동을 하는 것 또한 가중치 1로 취급 가능함 
// DFS로 풀이하게 될 경우 시간복잡도 큼 -> 동일 좌표를 중복으로 방문하게 되기 때문임 
// 최단거리를 찾는 문제로 BFS로 푸는 것이 적절하다 
// 주의할 점은 

public class Main {

    static int K, W, H;
    static int sr,sc,tr,tc; 
    static int[][] board;
    static boolean[][][] visited; // r,c,k
    static Queue<Node> q;

    // 상하좌우 탐색 
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    // 나이트 탐색 
    static int[] kdr = {-2, -1, 1, 2, 2, 1, -1, -2};
    static int[] kdc = {1, 2, 2, 1, -1, -2, -2, -1};

    static class Node {
        int r, c, k, moves;

        public Node(int r, int c, int k, int moves) {
            this.r = r;
            this.c = c;
            this.k = k; // 현재까지의 나이트 이동 횟수 
            this.moves = moves; // 최단 거리 업데이트용 전체 이동 횟수 
        }
    }

    public static void main(String[] args) throws Exception {
        
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st; 
    	
        K = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        W = Integer.parseInt(st.nextToken()); // 열 길이 
        H = Integer.parseInt(st.nextToken()); // 행 길이 
        
        sr = 0; sc = 0; tr = H-1; tc = W-1; 

        board = new int[H][W];
        for (int i = 0; i < H; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < W; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        visited = new boolean[H][W][K + 1]; // 나이트 이동 횟수는 0,1,2 ... K까지를 모두 카운트해야 하니까  
        System.out.println(bfs());
    }

    static int bfs() {
        q = new ArrayDeque<>(); 

        q.offer(new Node(sr, sc, 0, 0));// 시작 행, 시작 열, 나이트 사용 횟수, 총 이동 횟수 
        visited[0][0][0] = true;

        while (!q.isEmpty()) {
            Node curr = q.poll();
            int r = curr.r;
            int c = curr.c;
            int k = curr.k;
            int moves = curr.moves;

            if (r == tr && c == tc) {
                return moves;
            }

            // 1. 상하좌우 이동 
            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];

                // 장애물은 방문 불가 
                if (nr >= 0 && nr < H && nc >= 0 && nc < W && board[nr][nc] == 0) {
                    // 이미 nr,nc에 k번의 나이트를 사용해서 방문했다면 패스 
                	if (!visited[nr][nc][k]) {
                        visited[nr][nc][k] = true;
                        q.offer(new Node(nr, nc, k, moves + 1)); // 나이트 사용하지 않는 경우 
                    }
                }
            }

            // 2. 나이트 이동 -> 나이트 사용 횟수가 전체 나이트 가용 횟수보다 작아야 함 
            if (k < K) {
                for (int i = 0; i < 8; i++) {
                    int nr = r + kdr[i];
                    int nc = c + kdc[i];

                    // 장애물은 방문 불가 
                    if (nr >= 0 && nr < H && nc >= 0 && nc < W && board[nr][nc] == 0) {
                        // 현재 k번 나이트 이용했으니까 k+1번쨰 나이트 이용 셀 방문했는지 검사 
                        if (!visited[nr][nc][k + 1]) {
                            visited[nr][nc][k + 1] = true;
                            q.offer(new Node(nr, nc, k + 1, moves + 1));
                        }
                    }
                }
            }
        }


        return -1;
    }
}