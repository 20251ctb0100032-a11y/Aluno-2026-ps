/*
 * Disciplina: 2026-PS
 * Estudante: [Luiz Carlos Oliveira Neto]
 * Data      : [2026.08.27]
 * Projeto   : aula23-projeto-secretaria
 * Arquivo   : Main.java
 */

import java.util.ArrayList;
import java.util.Scanner;

/*
 * O BALCÃO DA SECRETARIA
 * Mostra o menu, lê a escolha e chama o método necessário.
 */

public class Main {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        // O GAVETEIRO
        ArrayList<Aluno> lista = new ArrayList<Aluno>();
        // Menu principal
        while (true) {
            System.out.println("----------------------------------");
            System.out.println("         SECRETARIA DO LC         ");
            System.out.println("----------------------------------");
            System.out.println("[1] Cadastrar aluno");
            System.out.println("[2] Listar alunos");
            System.out.println("[3] Buscar por matrícula");
            System.out.println("[4] Atualizar curso");
            System.out.println("[5] Remover aluno");
            System.out.println("[6] Relatorio");
            System.out.println("[0] Sair");
            System.out.print("Sua escolha: ");

            String opcao = teclado.nextLine().trim();

            // Texto se compara com .equals(), nunca com ==.
            if (opcao.equals("0")) {

                System.out.println("Secretaria fechada. Ate a proxima!");
                break;
            } else if (opcao.equals("1")) {
                cadastrar(lista, teclado);
            } else if (opcao.equals("2")) {
                listar(lista);
            } else if (opcao.equals("3")) {
                buscar(lista, teclado);
            } else if (opcao.equals("4")) {
                atualizar(lista, teclado);
            } else if (opcao.equals("5")) {
                remover(lista, teclado);
            } else if (opcao.equals("6")) {
                relatorio(lista, teclado);
            } else {

                System.out.println(
                    "Opcao invalida! Vale 0, 1, 2, 3, 4, 5 ou 6."
                );
            }
        }

        teclado.close();
    }

    // Cadastra um novo aluno.
    static void cadastrar(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Nome: ");
        String nome = teclado.nextLine().trim();
        System.out.print("Matricula: ");
        String matricula = teclado.nextLine().trim();

        // Verifica se a matrícula já está cadastrada.
        Aluno existente = buscarPorMatricula(lista, matricula);
        if (existente != null) {
            System.out.println(
                "Cadastro nao realizado: a matricula "
                + matricula
                + " ja esta cadastrada."
            );

            return;
        }

        System.out.print("Curso: ");
        String curso = teclado.nextLine().trim();
        Aluno novo = new Aluno(nome, matricula, curso);
        lista.add(novo);
        System.out.println("Ficha de " + novo.getNome() + " arquivada!");
    }

    // Lista todos os alunos.
    static void listar(ArrayList<Aluno> lista) {
        if (lista.size() == 0) {

            System.out.println("Nenhuma ficha no gaveteiro ainda.");
            return;
        }

        System.out.println(
            "--- FICHAS NO GAVETEIRO: " + lista.size() + " ---"
        );

        for (int i = 0; i < lista.size(); i++) {

            Aluno a = lista.get(i);

            System.out.println(
                a.getMatricula() + " | "
                + a.getNome() + " | "
                + a.getCurso()
            );
        }
    }

    // Procura um aluno pela matrícula.
    static Aluno buscarPorMatricula(
            ArrayList<Aluno> lista, String matricula) {

        for (int i = 0; i < lista.size(); i++) {

            Aluno a = lista.get(i);

            if (a.getMatricula().equals(matricula)) {
                return a;
            }
        }

        return null;
    }

    // Busca e mostra um aluno.
    static void buscar(ArrayList<Aluno> lista, Scanner teclado) {

        System.out.print("Matricula procurada: ");

        String matricula = teclado.nextLine().trim();

        Aluno a = buscarPorMatricula(lista, matricula);

        if (a == null) {

            System.out.println(
                "Nenhuma ficha com a matricula "
                + matricula + "."
            );

        } else {

            System.out.println(
                "Achei: "
                + a.getMatricula() + " | "
                + a.getNome() + " | "
                + a.getCurso()
            );
        }
    }

    // Atualiza o curso de um aluno.
    static void atualizar(ArrayList<Aluno> lista, Scanner teclado) {

        System.out.print("Matricula do aluno: ");

        String matricula = teclado.nextLine().trim();

        // Busca a ficha pela matrícula.
        Aluno a = buscarPorMatricula(lista, matricula);

        // Se não encontrou, encerra o método.
        if (a == null) {

            System.out.println(
                "Nenhuma ficha com a matricula "
                + matricula + "."
            );

            return;
        }

        // Pergunta o novo curso.
        System.out.print("Novo curso: ");

        String novoCurso = teclado.nextLine().trim();

        // Altera o curso da ficha encontrada.
        a.setCurso(novoCurso);

        System.out.println("Curso atualizado com sucesso!");
    }

    // Remove um aluno depois de pedir confirmação.
    static void remover(ArrayList<Aluno> lista, Scanner teclado) {

        System.out.print("Matricula do aluno: ");

        String matricula = teclado.nextLine().trim();

        // Busca a ficha pela matrícula.
        Aluno a = buscarPorMatricula(lista, matricula);

        // Se não encontrou, encerra o método.
        if (a == null) {

            System.out.println(
                "Nenhuma ficha com a matricula "
                + matricula + "."
            );

            return;
        }

        // Mostra o nome do dono da ficha.
        System.out.println("Ficha encontrada: " + a.getNome());

        // Pede confirmação antes de remover.
        System.out.print(
            "Tem certeza que deseja remover? (s/n): "
        );

        String confirmacao = teclado.nextLine().trim();

        if (confirmacao.equalsIgnoreCase("s")) {

            lista.remove(a);

            System.out.println("Ficha removida com sucesso!");

        } else {

            System.out.println("Remocao cancelada.");
        }
    }

    // RELATORIO: o padrao preparar -> percorrer -> usar, da Aula 29.
    static void relatorio(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.println("--- RELATORIO DA SECRETARIA ---");
        System.out.println("Total de fichas: " + lista.size());
        System.out.print("Contar alunos de qual curso? ");
        String curso = teclado.nextLine().trim();

        int contador = 0;                  // preparar (ANTES do for)
        for (int i = 0; i < lista.size(); i++) {  // percorrer
            Aluno a = lista.get(i);
            if (a.getCurso().equals(curso)) {
                contador = contador + 1;
            }
        }
        System.out.println("Alunos de " + curso + ": " + contador); // usar
    }
}