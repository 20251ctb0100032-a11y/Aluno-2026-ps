import java.util.Scanner;

public class desconto {

    static double calcularDesconto(double valor, double percentual) {
        return valor - (valor * percentual / 100);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite o valor: ");
        double valor = sc.nextDouble();

        System.out.print("Digite o percentual de desconto: ");
        double percentual = sc.nextDouble();

        double valorFinal = calcularDesconto(valor, percentual);

        System.out.println("Valor final: " + valorFinal);

        sc.close();
    }
}