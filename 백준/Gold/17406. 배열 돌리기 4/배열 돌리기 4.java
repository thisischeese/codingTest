import java.io.*;
import java.util.*;

public class Main {

    public static int N, M, K;
    public static int[][] arr,ops; 
    public static int[] opOrder;      
    public static boolean[] visited; 
    public static int minSum = Integer.MAX_VALUE;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        arr = new int[N][M];
        ops = new int[K][3];
        opOrder = new int[K];
        visited = new boolean[K];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            ops[i][0] = Integer.parseInt(st.nextToken()); // r
            ops[i][1] = Integer.parseInt(st.nextToken()); // c
            ops[i][2] = Integer.parseInt(st.nextToken()); // s
        }
        
        // 순열 생성 시작
        permMain(0);

        System.out.println(minSum);
        br.close();
    }

    // DFS
    public static void permMain(int depth) {
        if (depth == K) {
            // 원본 배열을 복사하여 사용
            int[][] tempArr = copyArray(arr);

            for (int i = 0; i < K; i++) {
                int opIdx = opOrder[i];
                int r = ops[opIdx][0];
                int c = ops[opIdx][1];
                int s = ops[opIdx][2];
                rotate(tempArr, r, c, s);
            }
            
            minSum = Math.min(minSum, calMinSum(tempArr));
            return;
        }

        for (int i = 0; i < K; i++) {
            if (!visited[i]) {
                visited[i] = true;
                opOrder[depth] = i;
                permMain(depth + 1);
                visited[i] = false; 
            }
        }
    }
    
    // 시계 방향 회전 
    public static void rotate(int[][] arr, int r, int c, int s) {
        for (int i = 1; i <= s; i++) {
            // 0-based 인덱스로 변환 및 현재 회전할 테두리의 경계 계산
            int top = r - i - 1;
            int left = c - i - 1;
            int bottom = r + i - 1;
            int right = c + i - 1;

            // 회전 시 덮어쓰기로 인해 사라질 왼쪽 위 값을 임시 저장
            int temp = arr[top][left];

            // 1. 왼 아래 -> 위
            for (int k = top; k < bottom; k++) {
                arr[k][left] = arr[k + 1][left];
            }
            // 2. 아래 오 -> 왼
            for (int k = left; k < right; k++) {
                arr[bottom][k] = arr[bottom][k + 1];
            }
            // 3. 오 위 -> 아래
            for (int k = bottom; k > top; k--) {
                arr[k][right] = arr[k - 1][right];
            }
            // 4. 위 왼 -> 오
            for (int k = right; k > left + 1; k--) {
                arr[top][k] = arr[top][k - 1];
            }
            
            arr[top][left + 1] = temp;
        }
    }

    // 각 행 최솟값 구하기 
    public static int calMinSum(int[][] arr) {
        int minSum = Integer.MAX_VALUE;
        for (int i = 0; i < N; i++) {
            int currentSum = 0;
            for (int j = 0; j < M; j++) {
                currentSum += arr[i][j];
            }
            minSum = Math.min(minSum, currentSum);
        }
        return minSum;
    }

    public static int[][] copyArray(int[][] src) {
        int[][] dest = new int[N][M];
        for (int i = 0; i < N; i++) {
            System.arraycopy(src[i], 0, dest[i], 0, M);
        }
        return dest;
    }
}