public class MaiorValor9 {

    // Método que recebe um array e retorna o maior valor
    static int maiorValor(int[] valores) {
        int maior = valores[0];

        for (int i = 1; i < valores.length; i++) {
            if (valores[i] > maior) {
                maior = valores[i];
            }
        }

        return maior;
    }

    // Método sobrecarregado que recebe dois números
    static int maiorValor(int a, int b) {
        if (a > b) {
            return a;
        } else {
            return b;
        }
    }

    public static void main(String[] args) {
        System.out.println(maiorValor(new int[]{3, 9, 5})); // 9
        System.out.println(maiorValor(12, 7));              // 12
        System.out.println(maiorValor(new int[]{4, 4, 4})); // 4
    }
}