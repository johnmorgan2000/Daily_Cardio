import java.util.Scanner;

public class Cardio {
    public static void main(String[] args){
        Scanner stdin = new Scanner(System.in);
        System.out.print("Num 1: ");
        int input1 = stdin.nextInt();
        System.out.print("Num 2: ");
        int input2 = stdin.nextInt();
        stdin.close();
        solution2(input1, input2);

    }

    public static void solution1(int input1, int input2){

        for (var i = 1; i <= input2; i++){
            int result = input1 * i;
            System.out.println(input1 + " * " + i + " = " + result );
        }
    }

    public static void solution2(int input1, int input2){
        int i = 1;
        while (i <= input2){
            int result = input1 * i;
            System.out.println(input1 + " * " + i + " = " + result );
            i++;
        }
    }

    public static int returnGreaterNum(int num1, int num2){
        if(num1 > num2){
            return num1;
        }
        return num2;
    }

    public static int getInput(String prompt){
        Scanner stdin = new Scanner(System.in);
        System.out.print(prompt);
        int input = stdin.nextInt();
        stdin.close();
        return input;
    }
}

