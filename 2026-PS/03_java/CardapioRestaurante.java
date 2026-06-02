import java.util.Scanner;

public class CardapioRestaurante {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        System.out.println("=================================");
        System.out.println("     RESTAURANTE DO ZEZINHO      ");
        System.out.println("=================================");
        System.out.println("     CARDÁPIO ELETRÔNICO");
        System.out.println("=================================");
        System.out.println("1 - X-Burguer .......... R$ 18,00");
        System.out.println("2 - Pizza .............. R$ 35,00");
        System.out.println("3 - Suco Natural ....... R$  8,00");
        System.out.println("4 - Café ............... R$  5,00");
        System.out.println("5 - Chá ................ R$  3,50");
        System.out.println("=================================");

        System.out.print("Escolha uma opção: ");
        int opcao = entrada.nextInt();

        // Substituição do switch por if, else if e else
        if (opcao == 1) {
            System.out.println("Você escolheu X-Burguer.");
            System.out.println("Valor: R$ 18,00");
        } else if (opcao == 2) {
            System.out.println("Você escolheu Pizza.");
            System.out.println("Valor: R$ 35,00");
        } else if (opcao == 3) {
            System.out.println("Você escolheu Suco Natural.");
            System.out.println("Valor: R$  8,00");
        } else if (opcao == 4) {
            System.out.println("Você escolheu Café.");
            System.out.println("Valor: R$  5,00");
        } else if (opcao == 5) {
            System.out.println("Você escolheu Chá.");
            System.out.println("Valor: R$  3,50");
        } else {
            System.out.println("Opção inválida. Por favor, escolha um número entre 1 e 5.");
        }

        entrada.close();
    }
}
