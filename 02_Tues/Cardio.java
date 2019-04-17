import java.util.Scanner;

public class Cardio {
    public static void main(String[] args){
        Scanner stdin = new Scanner(System.in);
        System.out.print("Num 1: ");
        int input1 = stdin.nextInt();
        solution1(input1);

        System.out.print("Num 2: ");
        int input2 = stdin.nextInt();
        solution2(input2);
        
        stdin.close();

    }

    public static void solution1(int input){
        for (var i = 1; i < input; i++){
            if(isFactor(i, input)){
                System.out.println(i + " is a factor of " + input);
            }
            else{
                System.out.println(i + " is NOT a factor of " + input);
            }
        }
    }

    public static void solution2(int input){
        int i = 1;
        while (i < input){
            if(isFactor(i, input)){
                System.out.println(i + " is a factor of " + input);
            }
            else{
                System.out.println(i + " is NOT a factor of " + input);
            } 
            i++;
        }
    }

    public static boolean isFactor(int num, int input){
        if (input % num == 0){
            return true;
        }
        return false;
    }
}
