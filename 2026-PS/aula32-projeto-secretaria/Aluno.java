/*
 * Disciplina 20260-PS
 * Estudante: Luiz Carlos Oliveira Neto
 * Data: 2026.08.13
 * Projeto: aula32-projeto-secretaria
 * Arquivo: Aluno.java
 */

public class Aluno {

    private String nome;
    private String matricula;
    private String curso;

    // Construtor que recebe nome, matrícula e curso.
    public Aluno(String nome, String matricula, String curso) {
        this.nome = nome;
        this.matricula = matricula;
        this.curso = curso;
    }

    // Retorna o nome do aluno.
    public String getNome() {
        return nome;
    }

    // Retorna a matrícula do aluno.
    public String getMatricula() {
        return matricula;
    }

    // Retorna o curso do aluno.
    public String getCurso() {
        return curso;
    }

    // Altera o nome do aluno.
    public void setNome(String nome) {
        this.nome = nome;
    }

    // Altera o curso do aluno.
    public void setCurso(String curso) {
        this.curso = curso;
    }
}