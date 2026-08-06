public class menorValor {

    public static void main(String[] args) {
        int[] numeros = {10, 5, 20, 8, 15};
        
        int resultado = menorValor(numeros);
        System.out.println("Menor valor: " + resultado);
    }

    static int menorValor(int[] numeros) {
        int menor = numeros[0];
        int it = 1;

        while (it < numeros.length) {
            if (numeros[it] < menor) {
                menor = numeros[it];
            }
            it++;
        }

        return menor;
    }
}