/*
 * Disciplina: 2026-PS
 * Projeto   : bibliotech
 * Arquivo   : Leitor.java
 * Autor     : Luiz Carlos Oliveira Neto
 * Descricao : Leitor E UM TIPO DE Usuario: herda nome, matricula
 */

public class Leitor extends Usuario {

    // So o que a caixa Leitor acrescenta. Nome e matricula ja vem de Usuario.
    private int limiteEmprestimos;
    private int livrosEmMaos; // nao estava na caixa: o codigo precisa controlar isso

    public Leitor(String nome, String matricula, int limiteEmprestimos) {
        super(nome, matricula); // Correção: Chamada correta do construtor do Usuario
        this.limiteEmprestimos = limiteEmprestimos;
        this.livrosEmMaos = 0;
    }

    public int getLimiteEmprestimos() {
        return limiteEmprestimos;
    }

    public int getLivrosEmMaos() {
        return livrosEmMaos;
    }

    // OPERAÇÃO DA CAIXA: podePegarEmprestado().
    public boolean podePegarEmprestado() {
        return livrosEmMaos < limiteEmprestimos;
    }

    // Os dois métodos que o empréstimo vai usar na Aula 38.
    public void pegueiLivro() {
        this.livrosEmMaos = this.livrosEmMaos + 1;
    }

    public void devolveuLivro() {
        this.livrosEmMaos = this.livrosEmMaos - 1;
    }

    @Override
    public String toString() {
        // Correção: Uso de getNome() em vez de 'this.nome', pois o atributo é private na classe pai
        return "Leitor: " + getNome() + " (" + getMatricula() + ") - "
                + livrosEmMaos + " de " + limiteEmprestimos + " livros";
    }
}
