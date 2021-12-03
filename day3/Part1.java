import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;
import java.lang.Math;

class Part1 {
    public static void main(String[] args) {
        int binaryLen = 12;
        int gammaRate = 0;
        int epsilonRate = 0;
        int powerConsumption = 0;
        int trueCount[] = new int[binaryLen];
        int falseCount[] = new int[binaryLen];
        int gammaBinary[] = new int[binaryLen];
        int epsilonBinary[] = new int[binaryLen];

        // Read files
        try {
            File input = new File("input.txt");
            Scanner scan = new Scanner(input);
            while (scan.hasNextLine()) {
                String binary = scan.nextLine();
                for (int i = 0; i < binary.length(); i++) {
                    char bit = binary.charAt(i);
                    if (bit == '1')
                        trueCount[i]++;
                    else
                        falseCount[i]++;
                }
            }
            System.out.println("True count: " + Arrays.toString(trueCount) + " False count: " + Arrays.toString(falseCount));
        } catch (FileNotFoundException e) {
            System.err.println("Error reading file");
            e.printStackTrace();
        }

        // Compare values
        for (int i = 0; i < binaryLen; i++) {
            if (trueCount[i] > falseCount[i]) {
                gammaBinary[i] = 1;
                epsilonBinary[i] = 0;
            }
            else if (trueCount[i] < falseCount[i]){
                gammaBinary[i] = 0;
                epsilonBinary[i] = 1;
            }
            else if (trueCount[i] == falseCount[i]) {
                gammaBinary[i] = 1;
                epsilonBinary[i] = 1;
            }
        }
        System.out.println("Gamma Binary: " + Arrays.toString(gammaBinary) + " Epsilon Binary: " + Arrays.toString(epsilonBinary));

        // Convert to decimal
        for (int i = 0; i < binaryLen; i++) {
            if (gammaBinary[i] == 1)
                gammaRate += Math.pow(2 * gammaBinary[i], binaryLen - i - 1);
            if (epsilonBinary[i] == 1)
                epsilonRate += Math.pow(2 * epsilonBinary[i], binaryLen - i - 1);
        }
        
        powerConsumption = gammaRate * epsilonRate;
        System.out.println("Gamma: " + gammaRate + " Epsilon: " + epsilonRate);
        System.out.println("Power consumption: " + powerConsumption);
    }
}