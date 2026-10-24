import java.util.ArrayList;
import java.util.List;

public class Biblioteca {
    private List<Livro> livros = new ArrayList<>();
    private List<Leitor> leitores = new ArrayList<>();
    private List<Emprestimo> emprestimos = new ArrayList<>();

    public void cadastrarLivro(Livro livro) {
        livros.add(livro);
    }

    public void cadastrarLeitor(Leitor leitor) {
        leitores.add(leitor);
    }

    public Livro buscarLivro(String titulo) {
        for (Livro l : livros) {
            if (l.getTitulo().equalsIgnoreCase(titulo)) {
                return l;
            }
        }
        return null;
    }

    public Leitor buscarLeitor(String matricula) {
        for (Leitor le : leitores) {
            if (le.getMatricula().equals(matricula)) {
                return le;
            }
        }
        return null;
    }

    public boolean emprestar(String titulo, String matricula) {
        Livro l = buscarLivro(titulo);
        Leitor le = buscarLeitor(matricula);

        if (l != null && le != null) {
            Emprestimo emp = new Emprestimo(l, le);
            if (emp.realizarEmprestimo()) {
                emprestimos.add(emp);
                return true;
            }
        }
        return false;
    }

    public void emprestarLivro(String titulo, String matricula) {
        emprestar(titulo, matricula);
    }

    public boolean devolver(String titulo) {
        for (Emprestimo e : new ArrayList<>(emprestimos)) {
            if (e.getLivro().getTitulo().equalsIgnoreCase(titulo) && e.isAtivo()) {
                if (e.registrarDevolucao()) {
                    emprestimos.remove(e);
                    return true;
                }
            }
        }
        return false;
    }

    public void devolverLivro(String titulo, String matricula) {
        devolver(titulo);
    }

    public void listarAcervo() {
        System.out.println("=== ACERVO ===");
        for (Livro l : livros) {
            System.out.println(l);
        }
    }

    public void listarEmprestimos() {
        System.out.println("=== EMPRÉSTIMOS ATIVOS ===");
        for (Emprestimo e : emprestimos) {
            if (e.isAtivo()) {
                System.out.println(e.getLivro().getTitulo() + " com " + e.getLeitor().getNome());
            }
        }
    }

    public String obterAcervoComoTexto() {
        if (livros.isEmpty()) {
            return "Nenhum livro cadastrado no acervo.";
        }
        StringBuilder sb = new StringBuilder();
        for (Livro l : livros) {
            sb.append(l.toString()).append("\n");
        }
        return sb.toString();
    }
}