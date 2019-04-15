import java.util.Scanner;

public class Cardio {
    public static void main(String[] args){
        Scanner stdin = new Scanner(System.in);
        System.out.print("Num: ");
        int input1 = Integer.parseInt(stdin.nextLine());
        iteration1(input1);

        System.out.print("Num 2: ");
        int input2 = Integer.parseInt(stdin.nextLine());
        iteration2(input2);

        stdin.close();


    }

    public static void iteration1(int input){
        for (int i = 1; i < input; i++){
            String type;
            if(isPositiveInt(i)){
                type = returnType(i);
                System.out.println(i + ":" + type);
            }
            else{
                System.out.println("invalid input");
            }  
        }
    }

    public static void iteration2(int input){
        int i = 1;
        while(i < input){
            String type;
            if(isPositiveInt(i)){
                type = returnType(i);
                System.out.println(i + ":" + type);
            }
            else{
                System.out.println("invalid input");
            }  
            i++;
        }
    }

    public static String returnType(int num){
        if(num % 2 == 0){
            return "Even";
        }else{
            return "Odd";
        }
    }

    public static boolean isPositiveInt(int num){
        if (num > 0){
            return true;
        }
        return false;
    }
}
