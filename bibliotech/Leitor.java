public class Leitor extends Usuario {
    private int limiteEmprestimos;
    private int livrosEnMaos;

    public Leitor(String nome, String matricula, int limiteEmprestimos) {
        super(nome, matricula);
        this.limiteEmprestimos = limiteEmprestimos;
        this.livrosEnMaos = 0;
    }

    public Leitor(String nome, String matricula) {
        this(nome, matricula, 2);
    }

    public int getLimiteEmprestimos() { return limiteEmprestimos; }
    public int getLivrosEnMaos() { return livrosEnMaos; }

    public boolean podePegarEmprestado() {
        return livrosEnMaos < limiteEmprestimos;
    }

    public void pegueiLivro() {
        if (podePegarEmprestado()) {
            livrosEnMaos++;
        }
    }

    public void devolviLivro() {
        if (livrosEnMaos > 0) {
            livrosEnMaos--;
        }
    }

    @Override
    public String toString() {
        return "Leitor: " + getNome() + " (Matrícula: " + getMatricula() + ")";
    }
}