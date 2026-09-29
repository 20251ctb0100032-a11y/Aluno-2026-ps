public class calculaMedia {

    public static void main(String[] args) {
        int[] numeros = {10, 5, 20, 8, 15};
        
        double resultado = calculaMedia(numeros);
        System.out.println("Média: " + resultado);
    }

    static double calculaMedia(int[] numeros) {
        double soma = 0;

        for (int i = 0; i < numeros.length; i++) {
            soma += numeros[i];
        }

        return soma / numeros.length;
    }
}