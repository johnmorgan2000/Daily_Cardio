import java.util.Scanner;

public class Cardio {
    public static void main(String[] args){
        Integer[] ints = {1, 0, 0, 0};
        solution2(ints);
    }

    public static void solution1(Integer[] ints){
        int ones = 0;
        int zeros = 0;
        for (int i : ints){
            if (i == 1){
                ones++;
            }else if (i == 0){
                zeros++;
            }
        }

        System.out.println(isMoreOnes(ones, zeros));
    }

    public static void solution2(Integer[] ints){
        int ones = 0;
        int zeros = 0;
        int i = 0;
        while (i < ints.length){
            if (i == 1){
                ones++;
            }else if (i == 0){
                zeros++;
            }
            i++;
        }

        System.out.println(isMoreOnes(ones, zeros));
    }


    public static boolean isMoreOnes( int ones, int zeros){
        if (ones > zeros){
            return true;
        }
        return false;
    }
}
