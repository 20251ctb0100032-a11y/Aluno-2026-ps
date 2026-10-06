import java.util.ArrayList;

public class Biblioteca {

    private ArrayList<Livro> livros;
    private ArrayList<Leitor> leitores;
    private ArrayList<Emprestimo> emprestimos;

    public Biblioteca() {
        livros = new ArrayList<Livro>();
        leitores = new ArrayList<Leitor>();
        emprestimos = new ArrayList<Emprestimo>();
    }

    public void cadastrarLivro(Livro livro) {
        livros.add(livro);
    }

    public void cadastrarLeitor(Leitor leitor) {
        leitores.add(leitor);
    }

    public void listarAcervo() {
        System.out.println("--- Acervo ---");

        for (Livro livro : livros) {
            System.out.println(livro);
        }
    }

    public Livro buscarLivro(String titulo) {
        for (Livro livro : livros) {
            if (livro.getTitulo().equals(titulo)) {
                return livro;
            }
        }

        return null;
    }

    public Leitor buscarLeitor(String matricula) {
        for (Leitor leitor : leitores) {
            if (leitor.getMatricula().equals(matricula)) {
                return leitor;
            }
        }

        return null;
    }

    public boolean emprestar(String titulo, String matricula) {
        Livro livro = buscarLivro(titulo);
        Leitor leitor = buscarLeitor(matricula);

        if (livro == null || leitor == null) {
            return false;
        }

        Emprestimo emprestimo = new Emprestimo(livro, leitor);

        if (!emprestimo.realizarEmprestimo()) {
            return false;
        }

        emprestimos.add(emprestimo);
        return true;
    }

    public boolean devolver(String titulo) {
        for (Emprestimo emprestimo : emprestimos) {
            if (emprestimo.estaAtivo()
                    && emprestimo.getLivro().getTitulo().equals(titulo)) {
                return emprestimo.registrarDevolucao();
            }
        }

        return false;
    }

    public void listarEmprestimos() {
        System.out.println("--- Emprestimos ---");

        for (Emprestimo emprestimo : emprestimos) {
            System.out.println(emprestimo);
        }
    }
}
