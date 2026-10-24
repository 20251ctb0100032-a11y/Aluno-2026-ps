public class Emprestimo {
    private Livro livro;
    private Leitor leitor;
    private boolean ativo;

    public Emprestimo(Livro livro, Leitor leitor) {
        this.livro = livro;
        this.leitor = leitor;
        this.ativo = false;
    }

    public Livro getLivro() { return livro; }
    public Leitor getLeitor() { return leitor; }
    public boolean isAtivo() { return ativo; }

    public boolean realizarEmprestimo() {
        if (livro != null && leitor != null && livro.estaDisponivel() && leitor.podePegarEmprestado()) {
            livro.emprestar();
            leitor.pegueiLivro();
            this.ativo = true;
            return true;
        }
        return false;
    }

    public boolean registrarDevolucao() {
        if (ativo && livro != null && leitor != null) {
            livro.devolver();
            leitor.devolviLivro();
            this.ativo = false;
            return true;
        }
        return false;
    }
}