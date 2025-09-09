import java.io.*;
import java.util.*;

public class Main {

    public static int[][] arr = new int[9][9];
    public static int[] rowv = new int[9];
    public static int[] colv = new int[9];
    public static int[][] sqrv = new int[3][3];

    public static StringBuilder sb = new StringBuilder();
    
    public static void bt(int idx) {
        if (idx == 81) {
            for (int i = 0; i < 9; i++) {
                for (int j = 0; j < 9; j++) {
                    sb.append(arr[i][j]);
                }
                sb.append("\n");
            }
            System.out.print(sb.toString());
            System.exit(0); // 사전순 정렬된 최초해만 찾기 
        }
        
        int r = idx / 9;
        int c = idx % 9;
        
        if (arr[r][c] != 0) {
            bt(idx + 1);
            return;
        }


        for (int num = 1; num <= 9; num++) {
            int bit = 1 << (num - 1);
            
            // 행, 열, 3*3 사각형 순으로 방문 여부 비트마스킹으로 확인 
            if ((rowv[r] & bit) == 0 && (colv[c] & bit) == 0 && (sqrv[r / 3][c / 3] & bit) == 0) {
                
                // 업데이트
                arr[r][c] = num;
                rowv[r] |= bit;
                colv[c] |= bit;
                sqrv[r / 3][c / 3] |= bit;
                
                // 재귀 
                bt(idx + 1);
                
                // 원상복귀
                arr[r][c] = 0;
                rowv[r] &= ~bit;
                colv[c] &= ~bit;
                sqrv[r / 3][c / 3] &= ~bit;
            }
        }
    }
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        for (int i = 0; i < 9; i++) {
            String s = br.readLine();
            for (int j = 0; j < 9; j++) {
                arr[i][j] = s.charAt(j) - '0';
                
                // 비트마스킹으로 방문 처리 초기화하기 
                if (arr[i][j] != 0) {
                    int bit = 1 << (arr[i][j] - 1);
                    rowv[i] |= bit;
                    colv[j] |= bit;
                    sqrv[i / 3][j / 3] |= bit;
                }
            }
        }

        
        bt(0);
        br.close();

    }

    
}