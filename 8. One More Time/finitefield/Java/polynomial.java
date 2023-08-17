package Java;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class polynomial {

    public static int mod(int a, int p) {
        return (a % p + p) % p;
    }

    public static int add(int a, int b, int p) {
        return mod(a+b,p);
    }

    public static int sub(int a, int b, int p) {
        return mod(a-b,p);
    }

    public static int mul(int a, int b, int p) {
        return mod(a*b,p);
    }

    public static int inv(int a, int p) {

        int t = 0, newt = 1;
        int r = p, newr = a;

        while (newr != 0) {
            int quotient = r / newr;
            int temp = t;
            t = newt;
            newt = temp - quotient * newt;
            temp = r;
            r = newr;
            newr = temp - quotient * newr;
        }

        if (t < 0) {
            t += p;
        }

        return t;

    }

    public static int div(int a, int b, int p) {
        return mul(a,inv(b,p),p);
    }

    public static int[] interpolate(int P, int d, List<Integer> x, List<Integer> y) {
        int[] p = new int[d];

        for (int i = 0; i < d; i++) {
            int product = 1;
            int[] t = new int[d];

            for (int j = 0; j < d; j++) {
                if (i != j) {
                    product = mul(product,sub(x.get(i), x.get(j),P),P);
                }
            }

            product = div(y.get(i), product,P);
            t[0] = product;

            for (int j = 0; j < d; j++) {
                if (i != j) {
                    for (int k = d - 1; k > 0; k--) {
                        t[k] = add(t[k],t[k - 1],P);
                        t[k - 1] = mul(t[k - 1],-x.get(j),P);
                    }
                }
            }

            for (int j = 0; j < d; j++) {
                p[j] = add(p[j],t[j],P);
            }
        }

        return p;
    }

    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Error: Please provide a prime number and a file path.");
            return;
        }
        
        Integer P = Integer.parseInt(args[0]);
        String path = args[1];
        File file = new File(path);
        if (!file.exists()) {
            System.out.printf("Error: The file at '%s' doesn't exist!\n", path);
            return;
        }

        List<Integer> x = new ArrayList<>();
        List<Integer> y = new ArrayList<>();
        
        try (Scanner scanner = new Scanner(file)) {
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                String[] split = line.split(" ");

                if (split.length != 2) {
                    System.out.println("Error: Invalid input format");
                    return;
                }

                x.add(Integer.parseInt(split[0]));
                y.add(Integer.parseInt(split[1]));
            }

            int[] p = interpolate(P,x.size(), x, y);
            for (int val : p) {
                System.out.print(val + " ");
            }
            System.out.println();
        } catch (FileNotFoundException e) {
            System.out.printf("Error: The file at '%s' doesn't exist!\n", path);
        } catch (NumberFormatException e) {
            System.out.println("Error: Invalid number format in the file");
        }
    }
}
