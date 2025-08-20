import java.io.*;
import java.util.*;

public class Main {

    public static class Node {
        int idx;
        int val;

        Node(int idx, int val) {
            this.idx = idx;
            this.val = val;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            Queue<Node> queue = new LinkedList<>();
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                queue.add(new Node(i, Integer.parseInt(st.nextToken())));
            }

            int printCount = 0; // 인쇄된 횟수

            while (!queue.isEmpty()) {
                Node current = queue.poll(); 
                boolean isPrintable = true;

                for (Node other : queue) {
                    if (other.val > current.val) {
                        isPrintable = false;
                        break;
                    }
                }

                if (isPrintable) { 
                    printCount++;
                    if (current.idx == M) {
                        sb.append(printCount).append("\n");
                        break; 
                    }
                } else { 
                    queue.add(current);
                }
            }
        }

        br.close();
        System.out.println(sb.toString());
    }
}