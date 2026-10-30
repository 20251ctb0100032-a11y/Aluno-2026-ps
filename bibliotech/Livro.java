public class Livro {
    private int id;
    private String titulo;
    private String autor;
    private int ano;
    private boolean emprestado;

    // Novo construtor (Fase 3) - Para criar objetos vindos do MariaDB (com ID)
    public Livro(int id, String titulo, String autor, int ano) {
        this.id = id;
        this.titulo = titulo;
        this.autor = autor;
        this.ano = ano;
        this.emprestado = false;
    }

    // Construtor original (Preservado) - Mantém compatibilidade com o restante do projeto
    public Livro(String titulo, String autor, int ano) {
        this.titulo = titulo;
        this.autor = autor;
        this.ano = ano;
        this.emprestado = false;
    }

    // Construtor sobrecarregado (Preservado)
    public Livro(String titulo, String autor) {
        this(titulo, autor, 0);
    }

    // Getters e Setters para o ID
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    // Demais Getters e Setters
    public String getTitulo() { return titulo; }
    public String getAutor() { return autor; }
    public int getAno() { return ano; }

    public boolean estaDisponivel() {
        return !emprestado;
    }

    public boolean isEmprestado() {
        return emprestado;
    }

    public void setEmprestado(boolean emprestado) {
        this.emprestado = emprestado;
    }

    public void emprestar() {
        this.emprestado = true;
    }

    public void devolver() {
        this.emprestado = false;
    }

    @Override
    public String toString() {
        String status = emprestado ? "[EMPRESTADO]" : "[DISPONÍVEL]";
        return id + " - " + status + " " + titulo + " - " + autor;
    }
}