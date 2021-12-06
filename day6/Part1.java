import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;

public class Part1 {
    public static void main(String[] args) {
        ArrayList<LanternFish> lanternFishGroup = new ArrayList<LanternFish>();
        ArrayList<Integer> initialState = getInitialState("input.txt");
        int totalDays = 80;

        System.out.println(initialState.toString());
        for(int age : initialState) {
            lanternFishGroup.add(new LanternFish(age, false));
        }
        for(int days = 0; days < totalDays; days++) {
            ArrayList<LanternFish> newLanternFishGroup = new ArrayList<LanternFish>();
            for(int i = 0; i < lanternFishGroup.size(); i++) {
                LanternFish curFish = lanternFishGroup.get(i);
                if(curFish.getDaysUntilBirth() == 0) 
                    lanternFishGroup.add(new LanternFish(8, true));
                curFish.passDay();
                newLanternFishGroup.add(i, curFish);
            }
            lanternFishGroup = newLanternFishGroup;
        }
        System.out.println(lanternFishGroup.size());
    }

    public static ArrayList<Integer> getInitialState(String filepath) {
        ArrayList<Integer> initialState = new ArrayList<Integer>();
        try {
            File input = new File(filepath);
            Scanner scan = new Scanner(input);
            String line = scan.nextLine();
            for (String value : line.split(",")) {
                initialState.add(Integer.parseInt(value));
            }
        } catch (FileNotFoundException e) {
            System.err.println("Error reading file");
            e.printStackTrace();
        }
        return initialState;
    }
}

class LanternFish {
    private int daysUntilBirth;
    private boolean isBaby = true;
    
    public LanternFish(int age, boolean isBaby) {
        this.daysUntilBirth = age;
        this.isBaby = isBaby;
    }

    public int getDaysUntilBirth() {
        return daysUntilBirth;
    }

    public void setDaysUntilBirth(int days) {
        this.daysUntilBirth = days;
    }

    public void passDay() {
        if (isBaby) {
            isBaby = false;
            return;
        }
        if (this.getDaysUntilBirth() == 0) {
            this.daysUntilBirth = 6;
        }
        else {
            this.daysUntilBirth--;
        }
    }

    public String toString() {
        return String.valueOf(daysUntilBirth);
    }
}