import java.io.*;
import java.util.*;

class TrieNode {
    TrieNode[] children = new TrieNode[10];
    boolean isEnd = false;
}

class Trie {
    TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    public void insert(String word) {
        TrieNode node = this.root;
        for (int i = 0; i < word.length(); i++) {
            int idx = word.charAt(i) - '0';
            if (node.children[idx] == null) {
                node.children[idx] = new TrieNode();
            }
            node = node.children[idx];
        }
        node.isEnd = true;
    }


    public boolean isPrefix(String word) {
        TrieNode node = this.root;
        for (int i = 0; i < word.length(); i++) {
            int idx = word.charAt(i) - '0';
            node = node.children[idx];
        }


        for (int i = 0; i < 10; i++) {
            if (node.children[i] != null) {
                return true;
            }
        }
        return false;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        while  (t>0){
            t--;
            int n = Integer.parseInt(br.readLine());
            String[] numbers = new String[n];
            Trie trie = new Trie();

            for (int i = 0; i < n; i++) {
                numbers[i] = br.readLine();
                trie.insert(numbers[i]);
            }

            boolean ok = true;
            for (String num : numbers) {
                if (trie.isPrefix(num)) {
                    ok = false;
                    break;
                }
            }

            if (ok) {
                sb.append("YES\n");
            } else {
                sb.append("NO\n");
            }
        }
        System.out.print(sb.toString());
    }
}