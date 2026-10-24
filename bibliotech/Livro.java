public class Livro {
    private String titulo;
    private String autor;
    private int ano;
    private boolean emprestado;

    public Livro(String titulo, String autor, int ano) {
        this.titulo = titulo;
        this.autor = autor;
        this.ano = ano;
        this.emprestado = false;
    }

    public Livro(String titulo, String autor) {
        this(titulo, autor, 0);
    }

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
        return status + " " + titulo + " - " + autor;
    }
}