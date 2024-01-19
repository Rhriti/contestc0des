import java.util.HashMap;
import java.util.Scanner;

public class Main {
    static HashMap<String, Integer> memo;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int testCases = scanner.nextInt();
        scanner.nextLine(); // Consume newline

        while (testCases-- > 0) {
            int n = scanner.nextInt();
            scanner.nextLine(); // Consume newline
            String s = scanner.nextLine();
            memo = new HashMap<>();

            System.out.println(f(0, 0, n, s));
        }
        scanner.close();
    }

    static int f(int index, int rem, int n, String s) {
        // Base case
        if (memo.containsKey(index + "," + rem)) {
            return memo.get(index + "," + rem);
        }

        if (index == n) {
            if (rem != 0) {
                return 0;
            } else {
                return 1;
            }
        }

        if (s.charAt(index) != '?') {
            int val = s.charAt(index) - '0';
            if (rem >= val) {
                memo.put(index + "," + rem, f(index + 1, rem - val, n, s));
                return memo.get(index + "," + rem);
            } else {
                memo.put(index + "," + rem, f(index + 1, 9 + rem - val, n, s));
                return memo.get(index + "," + rem);
            }
        } else {
            int count = 0;
            if (index != 0) {
                for (int j = 0; j < 10; j++) {
                    if (rem >= j) {
                        count += f(index + 1, rem - j, n, s);
                    } else {
                        count += f(index + 1, 9 + rem - j, n, s);
                    }
                }
            } else {
                for (int j = 1; j < 10; j++) {
                    if (rem >= j) {
                        count += f(index + 1, rem - j, n, s);
                    } else {
                        count += f(index + 1, 9 + rem - j, n, s);
                    }
                }
            }
            memo.put(index + "," + rem, count);
            return count;
        }
    }
}
