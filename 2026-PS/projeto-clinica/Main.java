import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    static Scanner teclado = new Scanner(System.in);
    static ArrayList<Produto> produtos = new ArrayList<>();

    public static void main(String[] args) {

        int opcao = 0;

        while (opcao != 5) {

            System.out.println("\n=== SISTEMA DE PRODUTOS ===");
            System.out.println("1 - Cadastrar");
            System.out.println("2 - Listar");
            System.out.println("3 - Alterar preço");
            System.out.println("4 - Remover");
            System.out.println("5 - Sair");
            System.out.print("Opção: ");

            opcao = teclado.nextInt();
            teclado.nextLine();

            // CORREÇÃO: caso o usuário digite uma opção inválida
            if (opcao == 1) {

                System.out.print("Código: ");
                int codigo = teclado.nextInt();
                teclado.nextLine();

                // CORREÇÃO: verifica se o código já existe
                boolean existe = false;

                for (Produto p : produtos) {
                    if (p.codigo == codigo) {
                        existe = true;
                        break;
                    }
                }

                if (existe) {
                    System.out.println("Erro: código já cadastrado!");
                    continue;
                }

                System.out.print("Nome: ");
                String nome = teclado.nextLine();

                System.out.print("Preço: ");
                double preco = teclado.nextDouble();

                // ERRO ORIGINAL:
                // Produto p = new Produto(codigo, nome, preco);
                //
                // A classe Produto não estava criada no seu código.
                // Agora ela está criada no final deste arquivo.

                Produto p = new Produto(codigo, nome, preco);
                produtos.add(p);

                System.out.println("Produto cadastrado com sucesso!");

            } else if (opcao == 2) {

                // CORREÇÃO: verifica se existem produtos
                if (produtos.isEmpty()) {

                    System.out.println("Nenhum produto cadastrado.");

                } else {

                    for (Produto p : produtos) {
                        System.out.println(
                            p.codigo + " - " +
                            p.nome + " - R$ " +
                            p.preco
                        );
                    }
                }

            } else if (opcao == 3) {

                System.out.print("Código: ");
                int codigo = teclado.nextInt();

                boolean encontrado = false;

                for (Produto p : produtos) {

                    if (p.codigo == codigo) {

                        System.out.print("Novo preço: ");
                        double preco = teclado.nextDouble();

                        p.preco = preco;

                        encontrado = true;

                        // CORREÇÃO:
                        // Como encontramos o produto, não precisamos
                        // continuar percorrendo a lista.
                        break;
                    }
                }

                // CORREÇÃO: avisa caso o código não exista
                if (!encontrado) {
                    System.out.println("Produto não encontrado.");
                } else {
                    System.out.println("Preço alterado com sucesso!");
                }

            } else if (opcao == 4) {

                System.out.print("Código: ");
                int codigo = teclado.nextInt();

                /*
                 * ERRO ORIGINAL:
                 *
                 * for (Produto p : produtos) {
                 *
                 *     if (p.codigo == codigo) {
                 *         produtos.remove(p);
                 *     }
                 * }
                 *
                 * O problema é que você estava removendo um produto
                 * da ArrayList enquanto percorria ela com um for-each.
                 *
                 * Isso pode causar:
                 *
                 * ConcurrentModificationException
                 *
                 * CORREÇÃO:
                 * Usamos removeIf(), que permite remover os produtos
                 * que atendem à condição.
                 */

                boolean removido = produtos.removeIf(p -> p.codigo == codigo);

                if (removido) {
                    System.out.println("Produto removido com sucesso!");
                } else {
                    System.out.println("Produto não encontrado.");
                }

            } else if (opcao == 5) {

                // O while vai terminar
                System.out.println("Saindo...");

            } else {

                // CORREÇÃO: trata opção inválida
                System.out.println("Opção inválida!");
            }
        }

        System.out.println("Sistema encerrado.");

        teclado.close();
    }
}


/*
 * ERRO ORIGINAL:
 *
 * A classe Produto não existia no código enviado.
 *
 * Como o programa usa:
 *
 * ArrayList<Produto>
 * Produto p
 * new Produto(...)
 *
 * precisamos criar essa classe.
 */

class Produto {

    int codigo;
    String nome;
    double preco;

    // Construtor da classe Produto
    Produto(int codigo, String nome, double preco) {

        this.codigo = codigo;
        this.nome = nome;
        this.preco = preco;
    }
}
