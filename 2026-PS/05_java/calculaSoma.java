public class calculaSoma {

    public static void main(String[] args) {
        int[] numeros = {10, 5, 20, 8, 15};
        
        int resultado = calculaSoma(numeros);
        System.out.println("Soma: " + resultado);
    }

    static int calculaSoma(int[] numeros) {
        int soma = 0;

        for (int n : numeros) {
            soma += n;
        }

        return soma;
    }
}