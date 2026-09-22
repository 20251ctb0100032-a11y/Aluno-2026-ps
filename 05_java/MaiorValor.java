public class maiorValor {

    public static void main(String[] args) {
        int[] numeros = {10, 5, 20, 8, 15};
        
        int resultado = maiorValor(numeros);
        System.out.println("Maior valor: " + resultado);
    }

    static int maiorValor(int[] numeros) {
        int maior = numeros[0];

        for (int n : numeros) {
            if (n > maior) {
                maior = n;
            }
        }

        return maior;
    }
}
