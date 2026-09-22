public class Top5 {

    static double calcularFrete(double peso) {
        if (peso <= 1) {
            return 10.00;
        } else if (peso <= 5) {
            return 20.00;
        } else {
            return 35.00;
        }
    }

    public static void main(String[] args) {
        System.out.println(calcularFrete(0.5)); // 10.0
        System.out.println(calcularFrete(1));   // 10.0
        System.out.println(calcularFrete(3));   // 20.0
        System.out.println(calcularFrete(5));   // 20.0
        System.out.println(calcularFrete(10));  // 35.0
    }
}