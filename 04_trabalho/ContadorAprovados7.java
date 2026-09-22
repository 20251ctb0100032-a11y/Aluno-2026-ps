public class ContadorAprovados7 {

    // Método estático que conta os alunos aprovados
    static int contarAprovados(double[] notas) {
        int aprovados = 0;

        for (int i = 0; i < notas.length; i++) {
            if (notas[i] >= 6.0) {
                aprovados++;
            }
        }

        return aprovados;
    }

    public static void main(String[] args) {
        double[] notas1 = {7.0, 4.0, 9.0, 6.0};
        double[] notas2 = {2.0, 3.0, 5.0};
        double[] notas3 = {10.0, 8.0, 6.0};

        System.out.println(contarAprovados(notas1)); // 3
        System.out.println(contarAprovados(notas2)); // 0
        System.out.println(contarAprovados(notas3)); // 3
    }
}