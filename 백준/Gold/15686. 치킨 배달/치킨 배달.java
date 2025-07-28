import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static List<int[]> houses = new ArrayList<>();
    static List<int[]> chickens = new ArrayList<>();
    static int total = Integer.MAX_VALUE;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        for (int r = 0; r < N; r++) {
            st = new StringTokenizer(br.readLine());
            for (int c = 0; c < N; c++) {
                int val = Integer.parseInt(st.nextToken());
                if (val == 1) houses.add(new int[]{r, c});
                else if (val == 2) chickens.add(new int[]{r, c});
            }
        }

        comb(0, 0, new int[M]);

        System.out.println(total);
        br.close();
    }

    static void comb(int start, int depth, int[] selected) {
        if (depth == M) {
            int cityDist = getDist(selected);
            total = Math.min(total, cityDist);
            return;
        }

        for (int i = start; i < chickens.size(); i++) {
            selected[depth] = i;
            comb(i + 1, depth + 1, selected);
        }
    }

    static int getDist(int[] selected) {
        int total = 0;
        for (int[] house : houses) {
            int minDist = Integer.MAX_VALUE;
            for (int idx : selected) {
                int[] chicken = chickens.get(idx);
                int dist = Math.abs(house[0] - chicken[0]) + Math.abs(house[1] - chicken[1]);
                minDist = Math.min(minDist, dist);
            }
            total += minDist;
        }
        return total;
    }
}
