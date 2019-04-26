class Cardio{
    public static void main(String[] args) {
        String magazine = "Hello world";
        String message = "HHe old";
        boolean answer = solution1(magazine, message);
        System.out.println(answer);
    }

    public static boolean solution1(String magazine, String message){
        char[] messLetters = message.toCharArray();

        for (char letter : messLetters){
            if (magazine.contains(String.valueOf(letter))|| letter == ' '){
                magazine = magazine.replaceFirst(String.valueOf(letter), "");
                continue;
            }
            else{
                return false;
            }
        }
        return true;
    }

    public static boolean solution2(String magazine, String message){
        char[] messLetters = message.toCharArray();
        int i = 0;

        while (i < messLetters.length){
            if (magazine.contains(String.valueOf(messLetters[i]))|| messLetters[i] == ' '){
                magazine = magazine.replaceFirst(String.valueOf(messLetters[i]), "");
                continue;
            }
            else{
                return false;
            }
        }
        return true;
    }
}

