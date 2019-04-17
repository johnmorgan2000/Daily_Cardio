import java.util.Scanner;

public class Cardio {
    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);

        System.out.print("String 1: ");
        String input1 = stdin.nextLine();

        System.out.print("String 2: ");
        String input2 = stdin.nextLine();

        // solution1(input1, input2);
        solution2(input1, input2);

    }

    public static void solution1(String input1, String input2) {
        String returnedString = "";
        for (var i = 0; i < returnConditionLength(input1, input2); i++) {

            if (input1.charAt(i) == input2.charAt(i)) {
                returnedString += input1.charAt(i);
            } else {
                returnedString += '.';
            }
        }
        System.out.println(returnedString);
    }

    public static void solution2(String input1, String input2) {
        String returnedString = "";
        char[] input1Array = input1.toCharArray();
        char[] input2Array = input2.toCharArray();

        int i = 0;
        while (i < input1Array.length){
            if (input1Array[i] == input2Array[i]){
                returnedString += input1Array[i];
            }
            else{
                returnedString += ".";
            }
            i++;
        }
        System.out.println(returnedString);

    }

    public static int returnConditionLength(String input, String input2) {
        if (input.length() > input2.length()) {
            return input.length();
        }
        return input2.length();
    }
}
