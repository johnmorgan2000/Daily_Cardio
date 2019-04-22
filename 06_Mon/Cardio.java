import java.util.Scanner;

public class Cardio {
    public static void main(String[] args){
        Integer[] ints = {10,0, 20, 10};
        solution2(ints);
    }

    public static void solution1(Integer[] ints){
        int largest = ints[0];
        int smallest = ints[0];
        for (int i = 0; i < ints.length; i++){
            largest = returnLargest(largest, ints[i]);
            smallest = returnSmallest(smallest, ints[i]);
        }
        System.out.println("Largest : " + largest);
        System.out.println("Smallest : " + smallest);
        System.out.println("Solution : " + (largest - smallest));
    }

    public static void solution2(Integer[] ints){
        int largest = ints[0];
        int smallest = ints[0];
        int i = 0;
        while (i < ints.length){
            largest = returnLargest(largest, ints[i]);
            smallest = returnSmallest(smallest, ints[i]);
            i++;
        }
        System.out.println("Largest : " + largest);
        System.out.println("Smallest : " + smallest);
        System.out.println("Solution : " + (largest - smallest));



    }

    public static int returnLargest(int largest, int currentInt){
        if (largest < currentInt){
            return currentInt;
        }
        return largest;
    }

    public static int returnSmallest(int smallest, int currentInt){
        if (smallest > currentInt){
            return currentInt;
        }
        return smallest;
    }
}
