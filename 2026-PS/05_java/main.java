public class Principal {

    public static void main(String[] args) {
        int[] numeros = {10, 5, 20, 8, 15};
        int limite = 10;

        System.out.println("--- RESULTADOS ---");
        System.out.println("Soma: " + calculaSoma(numeros));
        System.out.println("Média: " + calculaMedia(numeros));
        System.out.println("Menor valor: " + menorValor(numeros));
        System.out.println("Maior valor: " + maiorValor(numeros));
        System.out.println("Quantidade acima de " + limite + ": " + contarAcima(numeros, limite));
    }

    static int calculaSoma(int[] numeros) {
        int soma = 0;
        for (int n : numeros) {
            soma += n;
        }
        return soma;
    }

    static double calculaMedia(int[] numeros) {
        double soma = 0;
        for (int i = 0; i < numeros.length; i++) {
            soma += numeros[i];
        }
        return soma / numeros.length;
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

    static int maiorValor(int[] numeros) {
        int maior = numeros[0];
        for (int n : numeros) {
            if (n > maior) {
                maior = n;
            }
        }
        return maior;
    }

    static int contarAcima(int[] numeros, int limite) {
        int quantidade = 0;
        for (int i = 0; i < numeros.length; i++) {
            if (numeros[i] > limite) {
                quantidade++;
            }
        }
        return quantidade;
    }
}