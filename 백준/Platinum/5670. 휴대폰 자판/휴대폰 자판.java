import java.util.*;
import java.io.*;

public class Main {
    public static int N;
    public static String[] words;

    static class Node {
        Map<Character, Node> children = new HashMap<>();
        boolean isEnd = false;
        int passCnt = 0;
    }

    static class Trie {
        Node root;

        Trie() {
            this.root = new Node();
        }

        void insert(String word) {
            Node curr = this.root;
            for (char ch : word.toCharArray()) {
                curr.children.putIfAbsent(ch, new Node());
                curr = curr.children.get(ch);
                curr.passCnt++;
            }

            curr.isEnd = true;
        }

        int calCnt(String word) {
            int cnt = 0;
            Node curr = this.root;

            for (char ch : word.toCharArray()) {
                // 키를 눌러야 하는 경우
                // 1. 첫 글자 (curr == root)
                // 2. 여러 경로 분기되는 노드 (자식 사이즈 1보다 클 것 )
                // 3. 분기되지 않아도 isEnd값 true인 노드 
                if (curr == this.root || curr.children.size() > 1 || curr.isEnd) {
                    cnt++;
                }

                curr = curr.children.get(ch);
            }
            return cnt;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String line;

        while ((line = br.readLine()) != null && !line.isEmpty()) {
            N = Integer.parseInt(line);
            words = new String[N];
            Trie trie = new Trie();

            for (int i = 0; i < N; i++) {
                String word = br.readLine();
                words[i] = word;
                trie.insert(word);
            }

            double total = 0;

            for (int i = 0; i < N; i++) {
                total += trie.calCnt(words[i]);
            }
            
            double avg = total / N;
            sb.append(String.format("%.2f", avg)).append("\n");
        }

        br.close();
        System.out.print(sb.toString());
    }
}