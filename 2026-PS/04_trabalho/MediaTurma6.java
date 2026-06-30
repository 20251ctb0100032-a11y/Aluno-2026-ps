public class MediaTurma6 {

    // Método estático que calcula a média
    static double calcularMedia(double[] notas) {
        double soma = 0;

        for (int i = 0; i < notas.length; i++) {
            soma += notas[i];
        }

        return soma / notas.length;
    }

    public static void main(String[] args) {
        double[] notas1 = {7.0, 8.0, 9.0};
        double[] notas2 = {6.0, 6.0, 6.0, 6.0};
        double[] notas3 = {5.0, 10.0};

        System.out.println(calcularMedia(notas1)); // 8.0
        System.out.println(calcularMedia(notas2)); // 6.0
        System.out.println(calcularMedia(notas3)); // 7.5
    }
}