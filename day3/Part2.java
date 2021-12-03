import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Iterator;
import java.util.ArrayList;
import java.util.Scanner;
import java.lang.Math;

class Part2 {
    public static void main(String[] args) {
        int binaryLen = 12;
        int lifeSupportRating = 0;
        int oxygenRating = 0;
        int carbonRating = 0;
        ArrayList<String> oxygenList = new ArrayList<String>();
        ArrayList<String> carbonList = new ArrayList<String>();

        // Read files
        try {
            File input = new File("input.txt");
            Scanner scan = new Scanner(input);
            while (scan.hasNextLine()) {
                String binary = scan.nextLine();
                oxygenList.add(binary);
                carbonList.add(binary);
            }
        } catch (FileNotFoundException e) {
            System.err.println("Error reading file");
            e.printStackTrace();
        }

        // Ugly code : )
        // Iterate through each bit position
        for (int i = 0; i < binaryLen; i++) {
            Iterator<String> oxygenIterator = oxygenList.iterator();
            Iterator<String> carbonIterator = carbonList.iterator();
            int oxygenTrueCount = 0;
            int oxygenFalseCount = 0;
            int carbonTrueCount = 0;
            int carbonFalseCount = 0;

            // Count number of 1's and 0's
            while(oxygenIterator.hasNext()) {
                String binary = oxygenIterator.next();
                if (binary.charAt(i) == '1')
                    oxygenTrueCount++;
                else
                    oxygenFalseCount++;
            }
            while(carbonIterator.hasNext()) {
                String binary = carbonIterator.next();
                if (binary.charAt(i) == '1')
                    carbonTrueCount++;
                else
                    carbonFalseCount++;
            }

            // Remove entries that do not meet the criteria
            oxygenIterator = oxygenList.iterator();
            carbonIterator = carbonList.iterator();
            while(oxygenIterator.hasNext() && oxygenList.size() != 1) {
                if (oxygenTrueCount >= oxygenFalseCount && oxygenIterator.next().charAt(i) == '0')
                    oxygenIterator.remove();
                else if (oxygenTrueCount < oxygenFalseCount && oxygenIterator.next().charAt(i) == '1')
                    oxygenIterator.remove();

            }
            while(carbonIterator.hasNext() && carbonList.size() != 1) {
                if (carbonTrueCount < carbonFalseCount && carbonIterator.next().charAt(i) == '0')
                    carbonIterator.remove();
                else if (carbonTrueCount >= carbonFalseCount && carbonIterator.next().charAt(i) == '1')
                    carbonIterator.remove();
            }
        }

        // Convert to decimal
        String oxygenBinary = oxygenList.get(0);
        String carbonBinary = carbonList.get(0);
        for (int i = 0; i < binaryLen; i++) {
            if (oxygenBinary.charAt(i) == '1')
                oxygenRating += Math.pow(2 * Character.getNumericValue(oxygenBinary.charAt(i)), binaryLen - i - 1);
            if (carbonBinary.charAt(i) == '1')
                carbonRating += Math.pow(2 * Character.getNumericValue(carbonBinary.charAt(i)), binaryLen - i - 1);
        }
        lifeSupportRating = oxygenRating * carbonRating;
        System.out.println("Oxygen Rating: " + oxygenRating + " Carbon Rating: " + carbonRating + "\nLife Support Rating: " + lifeSupportRating);
    }
}