import java.util.*;

public class Main {
    static Map<Integer, Boolean> memo;
    static List<Integer> count;

    static boolean dfs(int[] arr, int node, int c, int k) {
        if (memo.containsKey(node)) {
            return memo.get(node);
        }

        count.set(node, c);
        int ch = arr[node];
        if (count.get(ch) == -1) {
            boolean local = dfs(arr, ch, c + 1, k);
            memo.put(node, local);
        } else {
            if (Math.abs(count.get(node) - count.get(ch)) + 1 == k) {
                memo.put(node, true);
            } else {
                memo.put(node, false);
            }
        }

        return memo.get(node);
    }

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            int t = scanner.nextInt();
            scanner.nextLine();

            while (t-- > 0) {
                int n = scanner.nextInt();
                int k = scanner.nextInt();
                scanner.nextLine();

                int[] arr = new int[n];
                count = new ArrayList<>(Collections.nCopies(n, -1));
                memo = new HashMap<>();

                for (int i = 0; i < n; i++) {
                    arr[i] = scanner.nextInt() - 1;
                }

                String finalResult = "YES";
                for (int i = 0; i < n; i++) {
                    count = new ArrayList<>(Collections.nCopies(n, -1));
                    boolean ans = dfs(arr, i, 0, k);
                    if (!ans) {
                        finalResult = "NO";
                        break;
                    }
                }
                System.out.println(finalResult);
            }
        }
    }
}
