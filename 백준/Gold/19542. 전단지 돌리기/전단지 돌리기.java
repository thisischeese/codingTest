import java.io.*;
import java.util.*;

public class Main {
    static int N, S, D;
    static List<Integer>[] graph;
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken()) - 1;
        D = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N];
        for (int i = 0; i < N; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken()) - 1;
            int v = Integer.parseInt(st.nextToken()) - 1;
            graph[u].add(v);
            graph[v].add(u);
        }

        dfs(S, -1);

        System.out.println(answer * 2);
    }

    static int dfs(int curr, int parent) {
        int maxDepth = 0;

        for (int next : graph[curr]) {
            if (next != parent) {
                int dist = dfs(next, curr) + 1;
                maxDepth = Math.max(maxDepth, dist);
            }
        }

        if (curr != S && maxDepth >= D) {
            answer++;
        }

        return maxDepth;
    }
}