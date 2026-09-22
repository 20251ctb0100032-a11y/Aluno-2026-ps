public class contarAcima {

    public static void main(String[] args) {
        int[] numeros = {10, 5, 20, 8, 15};
        int limite = 10;
        
        int resultado = contarAcima(numeros, limite);
        System.out.println("Quantidade acima de " + limite + ": " + resultado);
    }

    static int contarAcima(int[] numeros, int limite) {
        int quantidade = 0;

        for (int n : numeros) {
            if (n > limite) {
                quantidade++;
            }
        }

        return quantidade;
    }
}