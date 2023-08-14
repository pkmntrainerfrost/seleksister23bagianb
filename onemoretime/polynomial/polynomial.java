import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class polynomial {

    public static double[] interpolate(int d, List<Double> x, List<Double> y) {
        double[] p = new double[d];

        for (int i = 0; i < d; i++) {
            double product = 1.0;
            double[] t = new double[d];

            for (int j = 0; j < d; j++) {
                if (i != j) {
                    product *= (x.get(i) - x.get(j));
                }
            }

            product = y.get(i) / product;
            t[0] = product;

            for (int j = 0; j < d; j++) {
                if (i != j) {
                    for (int k = d - 1; k > 0; k--) {
                        t[k] += t[k - 1];
                        t[k - 1] *= (-x.get(j));
                    }
                }
            }

            for (int j = 0; j < d; j++) {
                p[j] += t[j];
            }
        }

        return p;
    }

    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Error: Please provide a file path.");
            return;
        }

        String path = args[0];
        File file = new File(path);
        if (!file.exists()) {
            System.out.printf("Error: The file at '%s' doesn't exist!\n", path);
            return;
        }

        List<Double> x = new ArrayList<>();
        List<Double> y = new ArrayList<>();

        try (Scanner scanner = new Scanner(file)) {
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                String[] split = line.split(" ");

                if (split.length != 2) {
                    System.out.println("Error: Invalid input format");
                    return;
                }

                x.add(Double.parseDouble(split[0]));
                y.add(Double.parseDouble(split[1]));
            }

            double[] p = interpolate(x.size(), x, y);
            for (double val : p) {
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
