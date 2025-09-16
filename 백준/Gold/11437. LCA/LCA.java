import java.io.*;
import java.util.*;

public class Main {

    public static int N, M;
    public static int[] pa, depth;
    public static ArrayList<Integer>[] arr;
    public static boolean[] v; 
    public static StringBuilder sb = new StringBuilder();

    public static void dfs(int current, int p, int d) {
        v[current] = true;
        pa[current] = p;
        depth[current] = d;

        for (int next : arr[current]) {
            if (!v[next]) {
                dfs(next, current, d + 1);
            }
        }
    }
    
    public static int findLCA(int a, int b) {
        // 2개의 포인터 깊이 맞추기 
        if (depth[a] < depth[b]) {
            int temp = a;
            a = b;
            b = temp;
        }

        // 같은 깊이 될 때까지 a만 부모로 계속 업데이트 
        while (depth[a] != depth[b]) {
            a = pa[a];
        }

        // 두 노드가 같을 때까지 2개의 포인터 모두 위로 계속 이동시키기 
        while (a != b) {
            a = pa[a];
            b = pa[b];
        }

        return a;
    }
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());

        pa = new int[N + 1];
        depth = new int[N + 1];
        v = new boolean[N + 1];
        
        arr = new ArrayList[N + 1];
        for (int i = 1; i <= N; i++) {
            arr[i] = new ArrayList<>();
        }


        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            arr[u].add(v);
            arr[v].add(u);
        }

        dfs(1, 0, 0);


        M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            sb.append(findLCA(u, v)).append("\n");
        }

        br.close();
        System.out.println(sb.toString());
    }

}