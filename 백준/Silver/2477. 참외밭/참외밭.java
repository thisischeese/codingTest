import java.io.*;
import java.util.*;

public class Main {

    public static int[][] info;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        int K = Integer.parseInt(br.readLine());

        info = new int[6][2];
        int maxWidth = 0, maxHeight = 0;
        int maxWidthIdx = -1, maxHeightIdx = -1;

        for (int i = 0; i < 6; i++) {
            st = new StringTokenizer(br.readLine());
            info[i][0] = Integer.parseInt(st.nextToken());
            info[i][1] = Integer.parseInt(st.nextToken());

            if (info[i][0] == 1 || info[i][0] == 2) {
                if (info[i][1] > maxWidth) {
                    maxWidth = info[i][1];
                    maxWidthIdx = i;
                }
            }
            else {
                if (info[i][1] > maxHeight) {
                    maxHeight = info[i][1];
                    maxHeightIdx = i;
                }
            }
        }

        int smallWidth, smallHeight;
        
        // 모듈러 연산 필요함 -> 꼭짓점이 끊어져도 순회할 수 있도록 
        int prev_w_idx = (maxWidthIdx + 5) % 6; 
        int next_w_idx = (maxWidthIdx + 1) % 6; 
        smallHeight = Math.abs(info[prev_w_idx][1] - info[next_w_idx][1]);

        int prev_h_idx = (maxHeightIdx + 5) % 6; 
        int next_h_idx = (maxHeightIdx + 1) % 6; 
        smallWidth = Math.abs(info[prev_h_idx][1] - info[next_h_idx][1]);

        int total = maxWidth * maxHeight;
        int target = smallWidth * smallHeight;
        
        sb.append(K * (total - target));
        br.close();
        System.out.println(sb.toString());
    }
}