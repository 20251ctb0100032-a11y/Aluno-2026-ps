public class BoletimTurma10 {

    // Exercício 1
    static double calcularMedia(double[] notas) {
        double soma = 0;

        for (int i = 0; i < notas.length; i++) {
            soma += notas[i];
        }

        return soma / notas.length;
    }

    // Exercício 2
    static int contarAprovados(double[] notas) {
        int aprovados = 0;

        for (int i = 0; i < notas.length; i++) {
            if (notas[i] >= 6.0) {
                aprovados++;
            }
        }

        return aprovados;
    }

    // Exercício 5
    static void exibirBoletim(double[] notas) {
        double media = calcularMedia(notas);
        int aprovados = contarAprovados(notas);

        System.out.println("Média: " + media);
        System.out.println("Aprovados: " + aprovados);

        if (media >= 6.0) {
            System.out.println("Situação: APROVADA");
        } else {
            System.out.println("Situação: EM RECUPERAÇÃO");
        }
    }

    public static void main(String[] args) {
        double[] notas1 = {7.0, 5.0, 9.0, 6.0};
        double[] notas2 = {4.0, 3.0, 5.0};

        exibirBoletim(notas1);
        System.out.println();
        exibirBoletim(notas2);
    }
}