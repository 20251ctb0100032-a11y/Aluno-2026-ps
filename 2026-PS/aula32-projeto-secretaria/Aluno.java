/*
* Disciplina 20260-PS
* Estudante: Luiz Carlos Oliveira Neto
* Data: 2026.08.13
* Projeto: aula32-projeto-secretaria
* Arquivo: Aluno.java
 */
 public class Aluno { /* cria a classe pubblica */
    private string nome; /* criando a variavel privada e tipo */
    private string matricula; /* criando a variavel privada e tipo */
    private string curso; /* criando a variavel privada e tipo */

    public Aluno(String nome, string matricula, string curso){
        this.nome = nome;
        this.matricula = matricula;
        this.curso = curso;
    }  /*E um construtor que recebe o nome, matricula e curso e guarda esses valores no objeto Aluno. */

    public string getNome() {
        return nome;
    } /*E um metodo que retorna o nome do aluno; getNome() serve para acessar o valor armazenado em nome. */

    public string getMatricula() {
        return matricula;
    } /*E um metodo que retorna o nome da Matricula; getMatricula() serve para acessar o valor armazenado em matricula. */

    public string getCurso() {
        return curso;
    } /*E um metodo que retorna o nome do curso; getCurso() serve para acessar o valor armazenado em curso. */


    public void setNome(string nome) {
        this.nome = nome;
    }
/*São métodos que alteram os dados do aluno: setNome() muda o nome e setCurso() muda o curso. */
    public void setCurso(string curso){
        this.curso = curso;
    }
 }