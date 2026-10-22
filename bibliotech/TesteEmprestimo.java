
public class TesteEmprestimo {

    public static void main(String[] args) {

        Livro livro = new Livro(
            "Dom Casmurro",
            "Machado de Assis",
            1899
        );

        Livro outroLivro = new Livro(
            "Capitães da Areia",
            "Jorge Amado",
            1937
        );

        Leitor pedro = new Leitor(
            "Pedro Alves",
            "2825010",
            1
        );

        Leitor ana = new Leitor(
            "Ana Lima",
            "2825011",
            2
        );

        // Primeiro empréstimo para Pedro
        Emprestimo primeiro = new Emprestimo(livro, pedro);

        System.out.println(
            "Primeiro empréstimo: "
            + primeiro.realizarEmprestimo()
        );

        System.out.println(primeiro);

        System.out.println(
            "Livro disponível? " + livro.estaDisponivel()
        );

        System.out.println(
            "Livros com Pedro: " + pedro.getLivrosEnMaos()
        );

        // Ana tenta pegar o mesmo livro
        Emprestimo tentativaAna = new Emprestimo(livro, ana);

        System.out.println(
            "Mesmo livro para Ana: "
            + tentativaAna.realizarEmprestimo()
        );

        // Pedro tenta pegar outro livro acima do limite
        Emprestimo tentativaPedro =
            new Emprestimo(outroLivro, pedro);

        System.out.println(
            "Pedro acima do limite: "
            + tentativaPedro.realizarEmprestimo()
        );

        System.out.println(
            "Outro livro ainda disponível? "
            + outroLivro.estaDisponivel()
        );

        // Devolução do primeiro livro
        System.out.println(
            "Devolução: " + primeiro.registrarDevolucao()
        );

        // Tentativa de devolver novamente
        System.out.println(
            "Segunda devolução: "
            + primeiro.registrarDevolucao()
        );

        // Pedro tenta pegar outro livro após a devolução
        System.out.println(
            "Outro livro para Pedro: "
            + tentativaPedro.realizarEmprestimo()
        );

        System.out.println(
            "Livros com Pedro: " + pedro.getLivrosEnMaos()
        );
    }
}
