import java.util.Random;
import java.util.Scanner;

public class FastFoodIFPR {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        Random random = new Random();
        String[] itens = {
            "X-Burguer",
            "Pizza",
            "Batata Frita",
            "Refrigerante",
            "Sorvete"
        };
        double[] precos = {
            18.00,
            35.00,
            21.00,
            8.00,
            6.00
        };
        int[] quantidades = new int[5];
        
        System.out.println("===============================");
        System.out.println("      FAST FOOD DA ESQUINA     ");
        System.out.println("===============================");
        
        int menuPrincipal = 1;
        while (menuPrincipal == 1) {
            // Loop para adição de itens
            int continuar = 1;
            while (continuar == 1) {
                System.out.println("\n1 - X-Burguer");
                System.out.println("2 - Pizza");
                System.out.println("3 - Batata Frita");
                System.out.println("4 - Refrigerante");
                System.out.println("5 - Sorvete");
                System.out.println("6 - Finalizar Pedido");

                System.out.print("\nEscolha: ");
                int opcao = entrada.nextInt();

                if (opcao >= 1 && opcao <= 5) {
                    System.out.print("\nQuantidade: ");
                    int qtd = entrada.nextInt();

                    quantidades[opcao - 1] += qtd;

                    System.out.println("\nItem adicionado ao pedido!");
                    System.out.println("\nDeseja continuar comprando?");
                    System.out.println("1 - Sim");
                    System.out.println("2 - Avançar");
                    System.out.print("\nEscolha: ");
                    continuar = entrada.nextInt();
                } else if (opcao == 6) {
                    continuar = 2;
                } else {
                    System.out.println("Opção inválida!");
                }
            }

            // Menu de gerenciamento: Voltar, Modificar ou Fechar
            System.out.println("\n=========================");
            System.out.println("   GERENCIAR PEDIDO");
            System.out.println("=========================");
            System.out.println("1 - Adicionar mais itens (Voltar)");
            System.out.println("2 - Alterar quantidade de um item (Modificar)");
            System.out.println("3 - Seguir para o pagamento");
            System.out.print("\nEscolha: ");
            int gerenciar = entrada.nextInt();

            if (gerenciar == 1) {
                // Não faz nada e o loop 'menuPrincipal' roda de novo
                menuPrincipal = 1;
            } else if (gerenciar == 2) {
                System.out.println("\nQual item deseja modificar?");
                for (int i = 0; i < itens.length; i++) {
                    System.out.printf("%d - %s (Atual: %d)%n", (i + 1), itens[i], quantidades[i]);
                }
                System.out.print("\nEscolha o número do item: ");
                int itemModificar = entrada.nextInt();

                if (itemModificar >= 1 && itemModificar <= 5) {
                    System.out.print("Digite a nova quantidade total para este item: ");
                    int novaQtd = entrada.nextInt();
                    quantidades[itemModificar - 1] = novaQtd;
                    System.out.println("\nQuantidade atualizada com sucesso!");
                } else {
                    System.out.println("\nItem inválido!");
                }
                // Permanece no menu de gerenciamento na próxima rodada
                menuPrincipal = 1;
            } else if (gerenciar == 3) {
                // Sai do loop e vai para o encerramento
                menuPrincipal = 2;
            } else {
                System.out.println("\nOpção inválida! Retornando ao menu.");
            }
        }

        System.out.println("\n=========================");
        System.out.println("      RESUMO DO PEDIDO");
        System.out.println("=========================");

        double total = 0;

        for (int i = 0; i < itens.length; i++) {
            if (quantidades[i] > 0) {
                double subtotal = quantidades[i] * precos[i];
                total += subtotal;

                System.out.printf(
                    "%dx %s ........ R$ %.2f%n",
                    quantidades[i],
                    itens[i],
                    subtotal
                );
            }
        }

        System.out.printf("\nTOTAL: R$ %.2f%n", total);
        System.out.println("\nForma de pagamento:");
        System.out.println("\n1 - Dinheiro");
        System.out.println("2 - Cartão");
        System.out.println("3 - PIX");
        System.out.print("\nEscolha: ");
        int pagamento = entrada.nextInt();

        if (pagamento >= 1 && pagamento <= 3) {
            System.out.println("\nPagamento realizado com sucesso!");
        } else {
            System.out.println("\nForma de pagamento inválida!");
        }

        int numeroPedido = random.nextInt(900) + 100;

        System.out.println("\nPedido Nº " + numeroPedido);
        System.out.println("\nAguarde a chamada do seu pedido.");

        entrada.close();
    }
}
