import java.util.Scanner;

public class Cardio{
    public static void main(String[] args){
        Scanner stdin = new Scanner(System.in);
        System.out.print("String 1: ");
        String input = stdin.nextLine();
        solution2(input);
        stdin.close();

        return;
    }

    public static void solution1(String input){
        String alpha = "abcdefghijklmnopqrstuvwxyz";

        // char[] alphaList = alpha.toCharArray();

        for(int i=0; i < input.length(); i++){
            char letter = input.charAt(i);
            char lowerCaseLetter = input.toLowerCase().charAt(i);
            int multi = alpha.indexOf(lowerCaseLetter)+1;
            String newString = "";
            for (int j=0; j < multi; j++){
                newString += letter;
            }
            System.out.println(newString);
            
        }
    }   
    public static void solution2(String input){
        String alpha = "abcdefghijklmnopqrstuvwxyz";

        for (char letter : input.toCharArray()) {
            int multi = alpha.indexOf(Character.toLowerCase(letter)) + 1;
            String newString = "";
            for (int i=0; i < multi; i++){
                newString += letter;
            }
            System.out.println(newString);
        }
    }

    
}
