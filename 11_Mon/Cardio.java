class Cardio{
    public static void main(String[] args) {
        double[] bill = {9.50, 11.75, 18.50, 3, 3};
        int allergyIndex = 0;
        int moneyGiven = 30;
        solution2(bill, allergyIndex, moneyGiven);

    }

    public static void solution1(double[] bill, int allergyIndex, int moneyGiven){
        double sharedPrice = 0;
        for (double price : bill){
            sharedPrice += price;

        }
        sharedPrice -= bill[allergyIndex];
        double cut = sharedPrice / 2;
        double diff = moneyGiven - cut;

        System.out.println(diff);
    }

    public static void solution2(double[] bill, int allergyIndex, int moneyGiven){
        double sharedPrice = 0;
        int i = 0;
        while (i < bill.length){
            sharedPrice += bill[i];
            i++;
        }
        sharedPrice -= bill[allergyIndex];
        double cut = sharedPrice / 2;
        double diff = moneyGiven - cut;
        System.out.println(diff);
    }
}
