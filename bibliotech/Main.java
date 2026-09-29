/*
 * Disciplina: 2026-PS
 * Projeto   : bibliotech
 * Arquivo   : Main.java
 * Autor     : Luiz Carlos Oliveiira Neto
 * Descricao : esqueleto do BiblioTech (Aula 36). Ainda nao faz nada:
 *             so prova que o ambiente compila e roda.
 */
public class Main {
    public static void main(String[] args) {
        System.out.println("BiblioTech v0.2 - as classes existem");

        Livro l1 = new Livro("Dom Casmurro", "Machado de Assis", 1899);
        Livro l2 = new Livro("Capitaes da Areia", "Jorge Amado", 1937);
        Leitor pedro = new Leitor("Pedro Alves", "2026010", 3);
        Bibliotecario marli = new Bibliotecario("Marli Souza", "199012", "1995");

        System.out.println(l1);
        System.out.println(l2);
        System.out.println(pedro);
        System.out.println(marli);

        // getNome() nao esta escrito em Leitor.java: veio de Usuar:
        System.out.println("Nome do leitor, via heranca: " + pedro.getNome());
        System.out.println("Pedro pode pegar livro? " + pedro.podePegarLivro());
        System.out.println("Marli entrou? " + marli.entrar());

        l1.emprestar();
        pedro.pegouLivro();
        System.out.println("Depois do emprestimo: " + l1);
        System.out.println("Depois do emprestimo: " + pedro);
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("BiblioTech v0.1 - esqueleto");
        System.out.println("Casos de uso planejados:");
        System.out.println("  1. Consultar disponibilidade");
        System.out.println("  2. Emprestar livro");
        System.out.println("  3. Devolver livro");
        System.out.println("  4. Identificar leitor");
    }
}