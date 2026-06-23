public class tj {

    // Soma de inteiros
    static int somar(int a, int b) {
        return a + b;
    }

    // Soma de números decimais
    static double somar(double a, double b) {
        return a + b;
    }

    public static void main(String[] args) {

        System.out.println(somar(5, 3));        // 8
        System.out.println(somar(2.5, 3.5));     // 6.0
        System.out.println(somar(100, 50));     // 150
    }
}